> **Fork notice**
>
> This is a fork of [Tasshack/dreame-vacuum](https://github.com/Tasshack/dreame-vacuum),
> based on v2.0.3, with one addition: the map keeps working when the robot is
> firewalled from Dreame's map storage.
>
> **What is different**
> - The last full map and downloaded map files are cached on disk
>   (`.storage/dreame_vacuum_map_cache/`) and reused after a restart when the
>   robot cannot deliver a new one.
> - Live position and path are drawn on the cached map when the robot starts a
>   new map but cannot upload it.
> - Rooms come with the cached map, so room entities and room cleaning keep
>   working.
>
> **What you need to allow for the robot**
> - Only the Dreame MQTT broker for your region (TCP 19973). Map storage can be
>   blocked once a map has been cached.
>
> **Limits**
> - The map is frozen at the last cached version. Changes made in the app
>   (rooms renamed, split or merged, no-go zones) only show up after you allow
>   map storage for one clean.
> - The first seconds of the path are missing on each clean, and the path can
>   have small gaps.
> - Cleaning history maps and obstacle photos are not available.
> - Tested on a Dreame X50 Ultra with a Dreamehome account only.
>
> **Install**: add this repository to HACS as a custom repository (type
> Integration), install, restart Home Assistant.
>
> Everything else below is the upstream README. All credit for the integration
> goes to [@Tasshack](https://github.com/Tasshack).

<center>
<div align="center">

<hr>
<a href="https://dreame-vacuum.tasshack.com/"><img alt="Dreame Vacuum" src="https://dreame-vacuum.tasshack.com/logo.svg" width=400></a>
<hr>

<a href="https://dreame-vacuum.tasshack.com/"><img alt="Dreame Vacuum" src="https://dreame-vacuum.tasshack.com/dvc.png" width=480 /></a>

Complete app replacement with **Home Assistant** for **Dreame** robot vacuums.

[![Version](https://img.shields.io/github/manifest-json/v/Tasshack/dreame-vacuum?filename=custom_components%2Fdreame_vacuum%2Fmanifest.json&color=18bcf2&label=Version&style=for-the-badge)](https://github.com/Tasshack/dreame-vacuum/releases)
![Downloads](https://img.shields.io/github/downloads/Tasshack/dreame-vacuum/total?label=Downloads&style=for-the-badge&color=18bcf2)
[![HACS](https://img.shields.io/badge/HACS-Default-orange.svg?logo=HomeAssistantCommunityStore&color=18bcf2&logoColor=white&style=for-the-badge)](https://github.com/hacs/integration)
[![Community Forum](https://img.shields.io/static/v1.svg?label=Community&message=Forum&color=18bcf2&logo=HomeAssistant&logoColor=white&style=for-the-badge)](https://community.home-assistant.io/t/custom-component-dreame-vacuum/473026)

</div>
</center>

<hr>

## Features

- Wide range of Dreame, MOVA, Mijia and Trouver robot vacuums and mops, configurable with a DreameHome, MovaHome, Xiaomi Home account or fully locally without the cloud
- Almost every setting and state exposed dynamically as auto generated entities
- Live and multi-floor map support with zone, spot and room cleaning
- Per-room suction, water volume and cleaning order for customized cleaning
- Persistent notifications and events for automations
- Cleaning/cruising history, obstacle photos, map backup & recovery and saved WiFi maps
- Backend translations for 40 languages
- Complete interactive map editor via embedded [Dreame Vacuum Card](https://dreame-vacuum-card.tasshack.com/)
<hr>

## [Documentation](https://dreame-vacuum.tasshack.com/)

- [Installation](https://dreame-vacuum.tasshack.com/installation) - Minimum Home Assistant version and hardware requirements, with [HACS](https://dreame-vacuum.tasshack.com/installation/hacs) and [manual](https://dreame-vacuum.tasshack.com/installation/manually) setup steps
- [Configuration](https://dreame-vacuum.tasshack.com/configuration) - Adding the device with a [Dreamehome](https://dreame-vacuum.tasshack.com/configuration/dreamehome), [Xiaomi Home](https://dreame-vacuum.tasshack.com/configuration/xiaomihome), [MOVAhome](https://dreame-vacuum.tasshack.com/configuration/movahome) or [TROUVER](https://dreame-vacuum.tasshack.com/configuration/trouver) account, or [locally](https://dreame-vacuum.tasshack.com/configuration/local) over the LAN
- [Configuration Options](https://dreame-vacuum.tasshack.com/configuration-options) - Per device settings offered during setup and from the Configure button
- [Supported Devices](https://dreame-vacuum.tasshack.com/guide/more/supported-devices) - Model codes of every tested [Dreame](https://dreame-vacuum.tasshack.com/guide/more/supported-devices#dreame), [MOVA](https://dreame-vacuum.tasshack.com/guide/more/supported-devices#mova), [Mijia](https://dreame-vacuum.tasshack.com/guide/more/supported-devices#mijia) and [TROUVER](https://dreame-vacuum.tasshack.com/guide/more/supported-devices#trouver) robot with the features it exposes
- [How to Use](https://dreame-vacuum.tasshack.com/guide) - How entities, services and events come together on a dashboard
- [Dashboard](https://dreame-vacuum.tasshack.com/guide/dashboard) - Setup examples and YAML templates for every supported Lovelace card, including the built-in **[Dreame Vacuum Card](https://dvc.tasshack.com/)**
- [Entities](https://dreame-vacuum.tasshack.com/guide/entities) - What gets generated for a device, with [map](https://dreame-vacuum.tasshack.com/guide/entities/map-entities), [room](https://dreame-vacuum.tasshack.com/guide/entities/room-entities) and [consumable](https://dreame-vacuum.tasshack.com/guide/entities/consumable-entities) entities covered separately
- [Map Support](https://dreame-vacuum.tasshack.com/guide/map-support) - How map data is decoded and rendered, with [history](https://dreame-vacuum.tasshack.com/guide/map-support/history), [recovery](https://dreame-vacuum.tasshack.com/guide/map-support/recovery), [obstacle photos](https://dreame-vacuum.tasshack.com/guide/map-support/obstacles) and [WiFi maps](https://dreame-vacuum.tasshack.com/guide/map-support/wifi-map)
- [Services](https://dreame-vacuum.tasshack.com/guide/services) - Parameters and automation examples for [device](https://dreame-vacuum.tasshack.com/guide/services/vacuum-services) and [map](https://dreame-vacuum.tasshack.com/guide/services/map-services) control
- [Notifications](https://dreame-vacuum.tasshack.com/guide/notifications) - Which device events raise a persistent notification and how to turn them off
- [Events](https://dreame-vacuum.tasshack.com/guide/events) - Event types fired on the bus and the payloads they carry
- [FAQ](https://dreame-vacuum.tasshack.com/guide/more/faq) - Recurring questions from the issue tracker and their actual causes

<hr>

## Thanks To

 - [xiaomi_vacuum](https://github.com/pooyashahidi/xiaomi_vacuum) by [@pooyashahidi](https://github.com/pooyashahidi)
 - [Xiaomi MIoT for Home Assistant](https://github.com/ha0y/xiaomi_miot_raw) by [@ha0y](https://github.com/ha0y)
 - [Xiaomi Cloud Map Extractor](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor) by [@PiotrMachowski](https://github.com/PiotrMachowski)
 - Dreame cloud authentication by [@kuudori](https://github.com/kuudori)
 - Mova cloud support by [@r1si](https://github.com/r1si)
