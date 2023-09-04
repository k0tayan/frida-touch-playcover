# Frida Touch for PlayCover
Make touch with Frida for PlayCover

## Requirements
- poetry
- yarn
- ipa

## Inject frida-gadget to IPA
- Install Sideloadly from https://sideloadly.io/
- Open Sideloadly, and open Advanced Options
- Check "Signing Mode" as "Export IPA"
- Check "Inject dylibs/Frameworks"
- Click "+dylib/deb/bundle" and select frida-gadget.dylib
- Click Start
- Install IPA to PlayCover

## Frida Config
- Open PlayCover
- Right click on the app and open in finder
- Open "AppName/Frameworks/"
- make "frida-gadget.config" file and write below

```frida-gadget.config
{
  "interaction": {
    "type": "listen",
    "address": "127.0.0.1",
    "port": 27042,
    "on_port_conflict": "fail",
    "on_load": "resume"
  }
}
```

## Install
```
poetry install
yarn install
```

## Build

```
yarn build
```

## Run

```
poetry run python example.py
```