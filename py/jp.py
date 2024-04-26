from api.jp.main import Api as BlueArchiveApiJP
from PIL import Image
import requests
import argparse
import string
import json
import os


def download_cg(api: BlueArchiveApiJP, out="jp/data/MediaResources/"):
    '''
    Download all CGs.
    '''
    resources = api.getMediaResources()
    # Filter resources that FileName ends with ".jpg"
    resources = [x for x in resources if x.fileName.endswith(".jpg")]
    for i, resource in enumerate(resources):
        # Check if already exists
        if os.path.exists(os.path.join(out, resource.path)):
            print(f"Skipping {resource.name}... ({i+1}/{len(resources)})")
            continue
        print(f"Downloading {resource.name}... ({i+1}/{len(resources)})")
        resource.setOutPath(out)
        resource.setKeepSubDir(True)
        resource.download()


def download_spinelobbies(api: BlueArchiveApiJP, out="jp/data/Andorid/"):
    '''
    Download all spinelobbies bundles.
    '''

    def validate_atlas(src=""):
        '''
        Validate atlas file and resize it if needed.
        '''
        with open(src, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            # Check if line contains size
            if line[0] == " ":
                continue
            if "size: " in line:
                # Get texture file, from line-1
                textureFile = lines[i-1].replace("\n", "").replace("\r", "")
                baseDir = os.path.dirname(src)

                # Get size
                width, height = [int(x) for x in line.split(" ")[1].split(",")]

                # Open texture file
                if not os.path.exists(f"{baseDir}/{textureFile}"):
                    print(f"Texture file {textureFile} not found!")
                    return False
                texture = Image.open(os.path.join(baseDir, textureFile))
                textureWidth, textureHeight = texture.size
                # Check if size is valid
                if width > textureWidth or height > textureHeight:
                    # Resize texture
                    print(f"Resizing {textureFile}...")
                    texture = texture.resize((width, height))
                    texture.save(os.path.join(baseDir, textureFile))
        return True

    def generate_info(directory="jp/data/Android/"):
        '''
        Create info.json that contains all .skel files.
        '''
        r = {}
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".skel"):
                    dir_name = os.path.basename(root)
                    dir_name = dir_name.replace(
                        "public/", "")  # Remove public/
                    if dir_name not in r:
                        r[dir_name] = []
                    full_file = os.path.join(root, file)
                    # Remove public/ from path
                    full_file = full_file.replace("public/", "")
                    full_file = full_file.replace("public\\", "")

                    r[dir_name].append(full_file)

        with open(os.path.join(directory, "info.json"), "w") as f:
            f.write(json.dumps(r, indent=4))

    bundles = api.getBundleInfo()
    # Filter bundles that contains "mx-spinelobbies-"
    bundles = [x for x in bundles if "mx-spinelobbies-" in x.name and x.name.split(
        "mx-spinelobbies-")[1][0] in string.ascii_letters]

    for i, bundle in enumerate(bundles):
        dir_name = bundle.name.split("-spinelobbies-")[1].split("-")[0]
        dest = os.path.join(out, dir_name)
        if os.path.exists(dest):
            continue
        # Check if bundle is already downloaded in temp
        temp_file = os.path.join("temp", bundle.name)
        if not os.path.exists(temp_file):
            bundle.download()
            print(f"Downloading {bundle.name}... ({i+1}/{len(bundles)})")
        print(f"Extracting {bundle.name}...")
        bundle.extract(f"temp/{bundle.name}", dest)

    generate_info(out)

    # Validate atlas files
    print("Validating atlas files...")
    for root, dirs, files in os.walk(out):
        for file in files:
            if file.endswith(".atlas"):
                validate_atlas(os.path.join(root, file))


def download_all(api: BlueArchiveApiJP, out="public/data/jp/"):
    '''
    Download spinelobbies and cg.
    '''
    print("Updating server info data url...")
    update_server_info_data_url(api)
    print("Updating MediaCatalog.json...")
    api.saveMediaCatalog(out=out)
    print("Downloading spinelobbies...")
    download_spinelobbies(api, out=out)
    print("Downloading cg...")
    download_cg(api, out=out)


def update_server_info_data_url(api: BlueArchiveApiJP):
    '''
    Update URL from updater and save it to version.json and url.tsx.
    '''
    api.updateURL()
    url = api.URL

    data = {}

    try:
        with open("./version.json", "r") as f:
            data = json.load(f)
    except:
        pass

    data["jp"]["url"] = url

    with open("./version.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    # Update url.tsx
        '''
        export const URL = "https://yostar-serverinfo.bluearchiveyostar.com/r62_18adige2364es3ybluha.json"; // 1.38
        export const AddressablesCatalogUrlRoot = "https://prod-clientpatch.bluearchiveyostar.com/r62_18adige2364es3ybluha_2";
        '''
    src = os.path.join("app", "jp", "url.tsx")
    r = requests.get(url)
    r = r.json()
    AddressablesCatalogUrlRoot = r["ConnectionGroups"][0]["OverrideConnectionGroups"][1]["AddressablesCatalogUrlRoot"]

    s = f'export const URL = "{url}";\nexport const AddressablesCatalogUrlRoot = "{AddressablesCatalogUrlRoot}";'

    with open(src, "w") as f:
        f.write(s)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--download", action="store_true", help="Download all")
    arg_parser.add_argument(
        "--download-cg", action="store_true", help="Download cg")
    arg_parser.add_argument(
        "--download-spine", action="store_true", help="Download spinelobbies")
    arg_parser.add_argument(
        "--update-url", action="store_true", help="Update URL from updater and save it to version.json and url.tsx")
    args = arg_parser.parse_args()

    api = BlueArchiveApiJP()
    if args.download:
        download_all(api)
    else:
        if args.download_cg:
            api.updateUrlFromCache()
            api.saveMediaCatalog(
                out="public/data/jp/MediaResources/")
            download_cg(api, out="public/data/jp/MediaResources/")
        elif args.download_spine:
            api.updateUrlFromCache()
            download_spinelobbies(api, out="public/data/jp/Android/")
        elif args.update_url:
            update_server_info_data_url(api)
        else:
            arg_parser.print_help()
