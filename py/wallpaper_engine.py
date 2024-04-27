from lib.wallpaper_engine.table import TableEN, TableJP
import json
import os
import re

project = {
    "title": "Blue Archive Live2D",
    "description": "Blue Archive Live2D Wallpaper",
    "file": "index.html",
    "preview": "icon.jpg",
    "general": {
        "properties": {
            "model": {
                "order": 1,
                "text": "Model",
                "type": "combo",
                "value": "circuit",  # replace this one
                "options": [
                    # Add models here.
                ]
            },
            "scale": {
                "order": 2,
                "text": "Scale",
                "type": "slider",
                "min": 0.1,
                "max": 1.5,
                "precision": 2,
                "step": 0.1,
                "value": 0.8
            },
            "play_voice": {
                "order": 3,
                "text": "Play Voice",
                "type": "bool",
                "value": False
            },
            "voice_volume": {
                "order": 4,
                "text": "Voice Volume",
                "type": "slider",
                "value": 100,
                "min": 0,
                "max": 100
            },
            "tap_to_talk": {
                "order": 5,
                "text": "Tap to Talk",
                "type": "bool",
                "value": False
            },
            "subtitle": {
                "order": 6,
                "text": "Subtitle",
                "type": "combo",
                "value": "none",
                "options": [
                    {
                        "label": "None",
                        "value": "none"
                    },
                    {
                        "label": "JP",
                        "value": "jp"
                    },
                    {
                        "label": "EN",
                        "value": "en"
                    }
                ]
            }
        }
    }
}

'''
const getLocalName = (s: string) => {
  // remove _home
  const devName = s.replace("_home", "");

  let dev = devName;
  let k = localizeCharFromDevName(devName);
  if (devName === k) {
    k = localizeCharFromDevName(`${devName}_default`);
    dev = `${devName}_default`;
    // Still not found
    if (k === `${devName}_default`) {
      k = localizeCharFromDevName(
        `${devName.substring(0, devName.length - 1)}_default`,
      );
      dev = `${devName.substring(0, devName.length - 1)}_default`;
      // Still not found
      if (k === `${devName.substring(0, devName.length - 1)}_default`) {
        k = s;
        dev = s;
      }
    }
  }
  return [k, dev];
};
'''


def resolve_path(src=""):
    '''
    Fix relative path for wallpaper engine.
    Replaces "/next..." with "./next..."
    '''
    data = ""
    with open(src, "r", encoding="utf-8") as f:
        data = f.read()

    data = data.replace("\"/_next", "\"./_next")

    with open(src, "w", encoding="utf-8") as f:
        f.write(data)


def get_characters():
    '''
    Get all character names from Blue Archive.
    '''
    jp = TableJP()
    en = TableEN()

    path_to_models = os.path.join(
        "public", "data", "jp", "Android", "info.json")
    with open(path_to_models, "r") as f:
        data = json.load(f)

    characters = []

    for key in data.keys():
        k = key.replace("_home", "")
        if en.localize_char_from_dev_name(k) is not None:
            characters.append(
                {
                    "label": en.localize_char_from_dev_name(k),
                    "value": key
                }
            )
        else:
            characters.append(
                {
                    "label": jp.localize_char_from_dev_name(k) or k,
                    "value": key
                }
            )

    return characters


def initialize_project():
    '''
    Initialize wallpaper engine project.
    '''

    characters = get_characters()
    project["general"]["properties"]["model"]["options"] = characters
    project["general"]["properties"]["model"]["value"] = characters[0]["value"]

    with open(os.path.join("wallpaper_engine", "project.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(project, indent=2, ensure_ascii=False))


def download_sounds():
    '''
    TODO
    '''
    pass


def main():
    for root, dirs, files in os.walk("./wallpaper_engine"):
        for file in files:
            if file.endswith(".html") or file.endswith(".js"):
                print(f"Resolving path for {file}")
                resolve_path(os.path.join(root, file))

    initialize_project()


if __name__ == "__main__":
    main()
