import os
import shutil


def build():
    # Remove old files
    if os.path.exists('./public/wallpaper_engine'):
        shutil.rmtree('./public/wallpaper_engine')

    os.makedirs('./public/wallpaper_engine', exist_ok=True)
    os.makedirs('./public/wallpaper_engine/_next/static', exist_ok=True)

    shutil.copy('./app/icon.jpg', './public/wallpaper_engine')
    shutil.copy('./.next/server/app/wpengine.html',
                './public/wallpaper_engine/index.html')
    shutil.copytree('./.next/server/app/wpengine',
                    './public/wallpaper_engine/wpengine', dirs_exist_ok=True)
    shutil.copytree('./.next/static',
                    './public/wallpaper_engine/_next/static', dirs_exist_ok=True)


if __name__ == '__main__':
    build()
