"use client";

import { Live2DViewer } from "@/app/lib/live2d_viewer";
import { useEffect } from "react";
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
  useEffect(() => {
    let options: Record<string, string | number | boolean> = {
      selectedModel: "airi0",
      scale: 0.8,
      playVoice: false,
      voiceVolume: 1,
      maxFPS: 30,
    };
    let models: Record<string, string[]> = {};
    // @ts-ignore
    window.wallpaperPropertyListener = {
      applyUserProperties: async function (properties: Record<string, any>) {
        if (properties.fps) {
          options.maxFPS = properties.fps.value as number;
          live2d.app.ticker.maxFPS = options.maxFPS;
        }
        if (properties.play_voice) {
          options.playVoice = properties.play_voice.value as boolean;
          live2d.playVoice = properties.play_voice.value;
        }
        if (properties.voice_volume) {
          options.voiceVolume = (properties.voice_volume.value as number) / 100;
          live2d.voiceVolume = properties.voice_volume.value;
        }
        if (properties.model) {
          options.selectedModel = properties.model.value as string;
          const model = models[options.selectedModel as string];

          for (let i = 0; i < model.length; i++) {
            const x = model[i];
            if (i == 0) await live2d.loadModel(x);
            else await live2d.addSpine(x, i.toString(), 0);
          }

          live2d.center();
          live2d.scale(options.scale as number);
          live2d.playAnimation("Start_Idle_01", {
            onComplete: () => {
              if (live2d.getAnimation("Idle_01") == null) return;

              live2d.playAnimation("Idle_01");
              live2d.loopAnimation = true;
            },
          });
        }
        if (properties.scale) {
          options.scale = properties.scale.value as number;
          live2d.scale(options.scale as number);
        }
      },
      applyGeneralProperties: async function (properties: Record<string, any>) {
      },
    };

    live2d = new Live2DViewer(document.getElementById("canvas") as HTMLCanvasElement);

    Table.initialize("jp").then(() => {
      fetchModels("./data/jp/Android/info.json").then(async (m) => {
        models = m;

        const base = get_origin();
        for (const [k, v] of Object.entries(models)) {
          models[k] = v.map((x) => base + "/" + x);
        }

        const model = models[options.selectedModel as string];
        const scale = options.scale as number;
        live2d.playVoice = options.playVoice as boolean;
        live2d.voiceVolume = options.voiceVolume as number;
        live2d.app.ticker.maxFPS = options.maxFPS as number;

        for (let i = 0; i < model.length; i++) {
          const x = model[i];
          if (i == 0) await live2d.loadModel(x);
          else await live2d.addSpine(x, i.toString(), 0);
        }

        live2d.center();
        live2d.scale(scale);
        live2d.playAnimation("Start_Idle_01", {
          onComplete: () => {
            if (live2d.getAnimation("Idle_01") == null) return;

            live2d.playAnimation("Idle_01");
            live2d.loopAnimation = true;
          },
        });
      });
    });
  });
  return (
    <div className="w-full h-full flex items-center justify-center">
      <canvas id="canvas">
      </canvas>
    </div>
  );
}
