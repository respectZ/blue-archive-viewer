# Blue Archive Viewer

[Live Preview](http://ba.svdex.moe/jp/live2d)

This is not affiliated nor nothing to do with Yostar.

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

Features:

- Supports EN and JP Server
- CG Gallery
- Live2D Viewer

The script to fetch the data is written using Rust.

## Fetching Data

You can run / build the Rust script.

```
Usage: blue-archive [OPTIONS] <COMMAND>

Commands:
  update
  help    Print this message or the help of the given subcommand(s)

Options:
  -r, --region <REGION>  [default: jp] [possible values: jp, en]
  -h, --help             Print help
  -V, --version          Print version
```

```
Usage: blue-archive.exe update <COMMAND>

Commands:
  catalog
  cg
  table
  live2-d
  all
  help     Print this message or the help of the given subcommand(s)

Options:
  -h, --help  Print help
```

Example:

```bash
blue-archive --region jp update all
```

To start the webserver:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Wallpaper Engine

There are two ways.

- You can download that includes every character at [releases](https://github.com/respectZ/blue-archive-viewer/releases).
- Or go to the [web](http://ba.svdex.moe/), navigate to the Live2D, and click the download as wallpaper engine button.

## Some weird cases

- [x] I don't know why the ch0152 jp version is missing `CH0152_home4.png` (seems like `CH0152` has multiple bundle files, so we need to check again if the file is unique instead of skipping it.)
- [x] there's `Hanako_home.skel` inside `hare_home` ???
- [x] `CH0996_home.atlas` should be renamed into `CH_9996.atlas`
- [x] `ibuki_home` should be renamed to `CH0077`

## Credits

- [K0lb3 BA Asset Downloader](https://github.com/K0lb3/Blue-Archive---Asset-Downloader)
