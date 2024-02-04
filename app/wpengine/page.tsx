"use client";

import { Live2DViewer } from "@/app/lib/live2d_wallpaper_engine";
import { useEffect, useRef, useState } from "react";
import * as Table from "@/app/lib/table";
import { get_origin } from "@/app/lib/get_origin";

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

export default function Home() {
  const [models, setModels] = useState<Record<string, string[]>>({});

  const [options, setOptions] = useState({
    selectedModel: "airi0_home",
    scale: 0.8,
    playVoice: false,
    voiceVolume: 1,
    tapToTalk: false,
    maxFPS: 60,
  });

  // You can update individual properties using setOptions
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
        await Table.initialize("jp");
        const m = await fetchModels("./data/jp/Android/info.json");
        setModels(m);
      };
      await initialize();
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [options.selectedModel]);

  useEffect(() => {
    (async () => {
      const reload = async () => {
        const model = models[options.selectedModel as string];

        for (let i = 0; i < model.length; i++) {
          const x = model[i];
          if (i == 0) await live2d.loadModel(x);
          else await live2d.addSpine(x, i.toString(), 0);
        }

        live2d.center();
        live2d.start();
      };

      if (Object.keys(models).length > 0) {
        await reload();
      }
    })();
  }, [options.selectedModel, models]);

  return (
    <div className="w-full h-full flex items-center justify-center">
      <canvas
        id="canvas"
        onClick={() => {
          if (options.tapToTalk) live2d.randomTalk();
        }}
      >
      </canvas>
    </div>
  );
}
