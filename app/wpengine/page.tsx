"use client";

import { localizeCharFromDevName } from "@/app/jp/live2d/character";
import { Live2DViewer } from "@/app/lib/live2d_wallpaper_engine";
import { createRef, useEffect, useRef, useState } from "react";
import * as Table from "./table";
import { getSubtitles } from "./subtitle";
import { ITrackEntry } from "pixi-spine";

let live2d: Live2DViewer;

async function fetchModels(file: string): Promise<Record<string, string[]>> {
  const models = await fetch(file).then((res) => res.json()) as Record<string, string[]>;
  // Remap key to actual model name
  const remapped = Object.keys(models).reduce((obj, item) => {
    const k = item;
    const v = models[item];
    obj[k] = v;
    return obj;
  }, {} as Record<string, string[]>);
  return remapped;
}

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

function showSubtitles(subtitle: HTMLDivElement, animationName: string, devName: string) {
  subtitle.innerHTML = "";
  const subtitles = getSubtitles(animationName, { devName: devName });
  for (const s of subtitles) {
    const p = document.createElement("p");
    p.innerText = s;
    p.classList.add("text-xl", "text-gray-200", "mb-2", "p-2", "bg-neutral-800", "bg-opacity-80");
    subtitle.appendChild(p);
  }
}

enum Subtitle {
  none = "none",
  en = "en",
  jp = "jp",
}

export default function Home() {
  const subtitle = createRef<HTMLDivElement>();
  const [models, setModels] = useState<Record<string, string[]>>({});
  const [l2dLoaded, setL2DLoaded] = useState(false);

  const [options, setOptions] = useState({
    selectedModel: "airi0_home",
    scale: 0.8,
    playVoice: false,
    voiceVolume: 1,
    tapToTalk: false,
    maxFPS: 60,
    subtitle: Subtitle.none,
  });
  const optionsRef = useRef(options);

  const updateSelectedModel = (newModel: string) => {
    setOptions((prevOptions) => ({
      ...prevOptions,
      selectedModel: newModel,
    }));
  };

  const updateScale = (newScale: number) => {
    setOptions((prevOptions) => ({
      ...prevOptions,
      scale: newScale,
    }));
  };

  const updatePlayVoice = (newPlayVoice: boolean) => {
    setOptions((prevOptions) => ({
      ...prevOptions,
      playVoice: newPlayVoice,
    }));
  };

  const updateVoiceVolume = (newVoiceVolume: number) => {
    setOptions((prevOptions) => ({
      ...prevOptions,
      voiceVolume: newVoiceVolume,
    }));
  };

  const updateTapToTalk = (newTapToTalk: boolean) => {
    setOptions((prevOptions) => ({
      ...prevOptions,
      tapToTalk: newTapToTalk,
    }));
  };

  const updateMaxFPS = (newMaxFPS: number) => {
    setOptions((prevOptions) => ({
      ...prevOptions,
      maxFPS: newMaxFPS,
    }));
  };

  const updateSubtitle = (newSubtitle: Subtitle) => {
    setOptions((prevOptions) => ({
      ...prevOptions,
      subtitle: newSubtitle,
    }));
  };

  useEffect(() => {
    optionsRef.current = options;
  }, [options]);

  useEffect(() => {
    // @ts-ignore
    window.wallpaperPropertyListener = {
      applyUserProperties: async function (properties: Record<string, any>) {
        if (properties.play_voice) {
          updatePlayVoice(properties.play_voice.value);
          live2d.playVoice = properties.play_voice.value;
        }
        if (properties.tap_to_talk) {
          updateTapToTalk(properties.tap_to_talk.value);
        }
        if (properties.voice_volume) {
          updateVoiceVolume(properties.voice_volume.value / 100);
          live2d.voiceVolume = properties.voice_volume.value / 100;
        }
        if (properties.model) {
          if (options.selectedModel !== properties.model.value as string) {
            updateSelectedModel(properties.model.value as string);
            if (Object.keys(models).length > 0 && live2d) {
              const model = models[options.selectedModel as string];

              for (let i = 0; i < model.length; i++) {
                const x = model[i];
                if (i == 0) await live2d.loadModel(x);
                else await live2d.addSpine(x, i.toString(), 0);
              }

              live2d.center();
              live2d.scale(options.scale as number);
              live2d.start();
            }
          }
        }
        if (properties.scale) {
          updateScale(properties.scale.value);
          live2d.scale(properties.scale.value);
        }
        if (properties.subtitle) {
          updateSubtitle(properties.subtitle.value);
        }
        optionsRef.current = options;
      },
      applyGeneralProperties: async function (properties: Record<string, any>) {
        if (properties.fps) {
          updateMaxFPS(properties.fps as number);
          live2d.app.ticker.maxFPS = properties.fps.value;
        }
      },
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    (async () => {
      if (Object.keys(models).length > 0) return;

      const initialize = async () => {
        if (live2d !== undefined) return;
        live2d = new Live2DViewer(document.getElementById("canvas") as HTMLCanvasElement);
        const m = await fetchModels("./data/jp/Android/info.json");
        setModels(m);
      };
      await initialize();
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [options.selectedModel]);

  useEffect(() => {
    setL2DLoaded(false);
    (async () => {
      const reload = async () => {
        const model = models[options.selectedModel as string];

        for (let i = 0; i < model.length; i++) {
          const x = model[i];
          if (i == 0) await live2d.loadModel(x);
          else await live2d.addSpine(x, i.toString(), 0);
        }
        setL2DLoaded(true);

        live2d.center();
        live2d.start();
      };

      if (Object.keys(models).length > 0) {
        await reload();
      }
    })();
  }, [options.selectedModel, models]);

  useEffect(() => {
    if (!l2dLoaded) return;

    const subtitleListener = {
      start: start,
      end: end,
    };

    function start() {
      const animation = live2d.currentAnimation;
      console.log(subtitle.current);
      if (!animation) return;
      if (!subtitle.current) return;
      subtitle.current.innerHTML = "";
      if (optionsRef.current.subtitle == Subtitle.none) return;
      const [_, devName] = getLocalName(optionsRef.current.selectedModel);
      console.log("showing subtitles");

      subtitle.current.classList.remove("opacity-0");
      subtitle.current.classList.add("opacity-100");
      showSubtitles(subtitle.current, animation, devName);
    }

    function end() {
      console.log("clearing subtitles");
      if (!subtitle.current) return;
      subtitle.current.classList.remove("opacity-100");
      subtitle.current.classList.add("opacity-0");
      setTimeout(() => {
        if (!subtitle.current) return;
        subtitle.current.innerHTML = "";
      }, 300);
    }

    live2d.setListener(subtitleListener);
  }, [subtitle, options.selectedModel, l2dLoaded]);

  useEffect(() => {
    if (options.subtitle == Subtitle.none) {
      if (!subtitle.current) return;
      subtitle.current.innerHTML = "";
    } else {
      Table.initialize(options.subtitle);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [options.subtitle]);

  return (
    <div className="w-full h-full flex items-center justify-center">
      <canvas
        id="canvas"
        onClick={() => {
          if (live2d.currentAnimation) return;
          if (!options.tapToTalk) return;
          live2d.randomTalk();
        }}
      >
      </canvas>
      <div className="w-auto h-auto fixed bottom-24 flex flex-col transition-all duration-300 opacity-100" ref={subtitle}></div>
    </div>
  );
}
