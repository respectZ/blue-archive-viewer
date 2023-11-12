from api.jp.main import Api as BlueArchiveApiJP
import os
import json
import string
from PIL import Image
import argparse


def downloadAll(out="jp/data/Android/"):
    api = BlueArchiveApiJP()
    bundles = api.getBundleInfo()
    # Filter bundles that contains "mx-spinelobbies-"
    bundles = [x for x in bundles if "mx-spinelobbies-" in x.name and x.name.split(
        "mx-spinelobbies-")[1][0] in string.ascii_letters]

    totalCount = len(bundles)
    count = 0
    for bundle in bundles:

        dirName = bundle.name.split("-spinelobbies-")[1].split("-")[0]
        dest = os.path.join(out, dirName)
        if os.path.exists(dest):
            count += 1
            continue
        # Check if bundle is already downloaded in temp
        tempFile = os.path.join("temp", bundle.name)
        if not os.path.exists(tempFile):
            bundle.download()
            print(f"Downloading {bundle.name}... ({count}/{totalCount})")
        print(f"Extracting {bundle.name}...")
        bundle.extract(f"temp/{bundle.name}", dest)
        count += 1


def validateAtlas(src=""):
    # Check if atlas is valid
    # In some cases, the atlas is bigger than the texture, so we need to resize it (Aru_home.atlas)
    with open(src, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        # Check if line contains size
        line = lines[i]
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
            texture = Image.open(f"{baseDir}/{textureFile}")
            textureWidth, textureHeight = texture.size
            # Check if size is valid
            if width > textureWidth or height > textureHeight:
                # Resize texture
                texture = texture.resize((width, height), Image.NEAREST)
                texture.save(f"{baseDir}/{textureFile}")
                print(f"Resized {textureFile} to {width}x{height}")
                return True


def generateInfo(directory="jp/data/Android/"):
    r = {}
    dirs = os.listdir(directory)
    for dir in dirs:
        dirName = os.path.join(directory, dir)
        if not os.path.isdir(dirName):
            continue
        r[dir] = []
        files = os.listdir(dirName)
        for file in files:
            if file.endswith(".skel"):
                noPublic = dirName.replace("public/", "")
                r[dir].append(os.path.join(noPublic, file))

        # IF len dir is more than 1, find _home.skel and move it to index 0
        if len(r[dir]) > 1:
            for i, file in enumerate(r[dir]):
                if "_home.skel" in file:
                    r[dir][0], r[dir][i] = r[dir][i], r[dir][0]
                    break
        # If no files found, remove dir
        if len(r[dir]) == 0:
            del r[dir]
    with open(os.path.join(directory, "info.json"), "w") as f:
        json.dump(r, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str,
                        default="public/data/jp/Android/", help="Output directory")
    args = parser.parse_args()

    print("Downloading...")
    downloadAll(out=args.out)

    print("Validating atlas...")

    for dir in os.listdir(args.out):
        d = os.path.join(args.out, dir)
        if not os.path.isdir(d):
            continue
        for file in os.listdir(d):
            if file.endswith(".atlas"):
                validateAtlas(os.path.join(d, file))

    print("Generating info...")

    generateInfo(args.out)

    print("Done!")
