from api.en.main import Api as BlueArchiveApiEN
from PIL import Image
import argparse
import string
import json
import os

# No need hassle to redownload all files, just reuse from jp.


def download_spinelobbies(api: BlueArchiveApiEN, check="jp/data/Android/", out="en/data/GameData/Android/"):
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

    def generate_info(d1, d2):
        '''
        Create info.json that contains all .skel files.
        '''
        r = {}
        ex = False
        directories = [d1, d2]
        for d in directories:
            for root, dirs, files in os.walk(d):
                for file in files:
                    if file.endswith(".skel"):
                        dir_name = os.path.basename(root)
                        dir_name = dir_name.replace(
                            "public/", "")  # Remove public/
                        if ex and dir_name in r:  # Already exists, either in en/jp
                            continue
                        if dir_name not in r:
                            r[dir_name] = []
                        full_file = os.path.join(root, file)
                        # Remove public/ from path
                        full_file = full_file.replace("public/", "")
                        full_file = full_file.replace("public\\", "")

                        r[dir_name].append(full_file)
            ex = True

        # Sort r by key
        r = dict(sorted(r.items(), key=lambda x: x[0]))

        dest = os.path.join("public", "data", "en",
                            "GameData", "Android", "info.json")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as f:
            f.write(json.dumps(r, indent=4))

    resources = api.resources
    # Filter spinelobbies
    resources = [x for x in resources if "mx-spinelobbies-" in x.resource_path and x.resource_path.split(
        "mx-spinelobbies-")[1][0] in string.ascii_letters]

    for i, resource in enumerate(resources):
        dir_name = resource.resource_path.split(
            "-spinelobbies-")[1].split("-")[0]
        dest = os.path.join(out, dir_name)
        if os.path.exists(dest) or os.path.exists(os.path.join(check, dir_name)):
            print(f"Skipping {dir_name}... ({i+1}/{len(resources)})")
            continue
        # Check if resource is already downloaded in temp
        filename = resource.resource_path.split("/")[-1]
        temp_file = os.path.join("temp", filename)
        if not os.path.exists(temp_file):
            resource.setOutPath("temp/")
            print(f"Downloading {filename}... ({i+1}/{len(resources)})")
            resource.download()

        print(f"Extracting {filename}...")
        resource.extractBundle(temp_file, dest)

    generate_info(check, out)

    # Validate atlas files
    print("Validating atlas files...")
    for root, dirs, files in os.walk(out):
        for file in files:
            if file.endswith(".atlas"):
                validate_atlas(os.path.join(root, file))


if __name__ == "__main__":
    api = BlueArchiveApiEN()
    download_spinelobbies(
        api,
        check=os.path.join("public", "data", "jp", "Android"),
        out=os.path.join("public", "data", "en", "GameData", "Android"),
    )
