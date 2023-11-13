# Blue Archive Viewer

This is not affiliated nor nothing to do with Yostar.

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

Features:
- Supports EN and JP Server
- CG Gallery
- Live2D Viewer

## Requirements
- Python 3.6+
- Node 1.10.6+

Installing python requirements:

```bash
pip install -r requirements.txt
```

## Getting Started

First, fetch the needed data:
```bash
python run py/main.py
```

To start the webserver:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Updating version
<!-- TODO -->
TODO

- Update `dump.cs`
- Run table fetcher

## TODO
- [ ] Create a workflow + script for updating `dump.cs` instead doing it manually
- [ ] Script for fetching `TableBundles`
- [x] EN Version
- [ ] Support wallpaper engine

## Bugs
- [ ] I don't know why the ch0152 jp version is missing `CH0152_home4.png` (seems like `CH0152` has multiple bundle files, so we need to check again if the file is unique instead of skipping it.)
- [ ] there's `Hanako_home.skel` inside `hare_home` ???

## Credits
- [K0lb3 BA Asset Downloader](https://github.com/K0lb3/Blue-Archive---Asset-Downloader)