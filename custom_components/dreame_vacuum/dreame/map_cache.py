"""On-disk cache for map data downloaded from the cloud.

The map manager only keeps maps in memory, so after a restart it depends on the
device uploading a fresh map to the cloud storage. When the device is not allowed
to reach that storage (firewalled) no map is ever received again. This cache keeps
the last full map frame and every downloaded map object on disk so they can be
used as a fallback.
"""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import os
import threading
import time
from typing import Optional, Tuple

_LOGGER = logging.getLogger(__name__)

MAP_FILE = "map.json"
OBJECT_DIR = "objects"
# Full frames can arrive every few seconds while cleaning, no need to write all of them
MIN_MAP_WRITE_INTERVAL = 30


class DreameVacuumMapCache:
    def __init__(self, path: str) -> None:
        self._path = path
        self._lock = threading.Lock()
        self._map_hash: Optional[str] = None
        self._map_write_time: float = 0
        self._object_hash: dict[str, str] = {}

    @staticmethod
    def _hash(data: bytes) -> str:
        return hashlib.sha1(data).hexdigest()

    def _object_path(self, object_name: str) -> str:
        return os.path.join(self._path, OBJECT_DIR, f"{self._hash(object_name.encode())}.json")

    def _write(self, path: str, payload: dict) -> bool:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            tmp_path = f"{path}.tmp"
            with open(tmp_path, "w", encoding="utf8") as file:
                json.dump(payload, file, separators=(",", ":"))
            os.replace(tmp_path, path)
            return True
        except Exception as ex:
            _LOGGER.warning("Map cache write failed %s: %s", path, ex)
            return False

    def _read(self, path: str) -> Optional[dict]:
        try:
            if not os.path.isfile(path):
                return None
            with open(path, "r", encoding="utf8") as file:
                payload = json.load(file)
            return payload if isinstance(payload, dict) else None
        except Exception as ex:
            _LOGGER.warning("Map cache read failed %s: %s", path, ex)
            return None

    def save_map(self, raw_map: str, key: Optional[str], timestamp: Optional[int]) -> None:
        """Store the last full (I frame) map as received from the device or the cloud."""
        if not raw_map:
            return
        map_hash = self._hash(f"{raw_map}|{key}".encode())
        with self._lock:
            now = time.time()
            if map_hash == self._map_hash or now - self._map_write_time < MIN_MAP_WRITE_INTERVAL:
                return
            if self._write(
                os.path.join(self._path, MAP_FILE),
                {"raw_map": raw_map, "key": key, "timestamp": timestamp, "saved": int(now)},
            ):
                self._map_hash = map_hash
                self._map_write_time = now

    def load_map(self) -> Optional[Tuple[str, Optional[str], Optional[int]]]:
        with self._lock:
            payload = self._read(os.path.join(self._path, MAP_FILE))
        if not payload or not payload.get("raw_map"):
            return None
        return payload["raw_map"], payload.get("key"), payload.get("timestamp")

    def save_object(self, object_name: str, data: bytes, key: Optional[str] = None) -> None:
        """Store a file downloaded from the cloud storage."""
        if not object_name or not data:
            return
        object_hash = self._hash(data + f"|{key}".encode())
        with self._lock:
            if self._object_hash.get(object_name) == object_hash:
                return
            if self._write(
                self._object_path(object_name),
                {
                    "object_name": object_name,
                    "key": key,
                    "data": base64.b64encode(data).decode("ascii"),
                    "saved": int(time.time()),
                },
            ):
                self._object_hash[object_name] = object_hash

    def load_object(self, object_name: str, key: Optional[str] = None) -> Optional[bytes]:
        """Return a previously downloaded file, only when it was stored with the same key."""
        if not object_name:
            return None
        with self._lock:
            payload = self._read(self._object_path(object_name))
        if not payload or not payload.get("data") or payload.get("key") != key:
            return None
        try:
            return base64.b64decode(payload["data"])
        except Exception as ex:
            _LOGGER.warning("Map cache decode failed %s: %s", object_name, ex)
            return None
