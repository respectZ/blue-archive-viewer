import { createSignal, createEffect, onCleanup, onMount } from "solid-js";
import { Live2DWallpaperEngine } from "~/lib/live2d-wallpaper-engine";
import { Live2DCanvas } from "~/components/Live2DCanvas";
import * as Table from "../lib/table";
import { getSubtitles } from "../lib/live2d/subtitle";
import { localizeCharFromDevName } from "../lib/live2d/character";

enum Subtitle {
  none = "none",
  en = "en",
  jp = "jp",
}

async function fetchModels(file: string): Promise<Record<string, string[]>> {
  const res = await fetch(file);
  const models = await res.json() as Record<string, string[]>;
  return models;
}

function getLocalName(s: string): [string, string] {
  const devName = s.replace("_home", "");
  let dev = devName;
  let k = localizeCharFromDevName(devName);
  if (devName === k) {
    k = localizeCharFromDevName(`${devName}_default`);
    dev = `${devName}_default`;
    if (k === `${devName}_default`) {
      k = localizeCharFromDevName(`${devName.substring(0, devName.length - 1)}_default`);
      dev = `${devName.substring(0, devName.length - 1)}_default`;
      if (k === `${devName.substring(0, devName.length - 1)}_default`) {
        k = s;
        dev = s;
      }
    }
  }
  return [k, dev];
}

function showSubtitles(subtitle: HTMLDivElement, animationName: string, devName: string) {
  subtitle.innerHTML = "";
  const subtitles = getSubtitles(animationName, { devName });
  for (const s of subtitles) {
    const p = document.createElement("p");
    p.innerText = s;
    p.classList.add("mb-2", "rounded-lg", "border", "border-[var(--border)]", "bg-[var(--bg-base)]/80", "p-2", "text-lg", "text-[var(--text-primary)]", "backdrop-blur");
    subtitle.appendChild(p);
  }
}

export function WPExport() {
  let engine: Live2DWallpaperEngine | undefined;
  let canvasRef: HTMLCanvasElement | undefined;
  let subtitleRef: HTMLDivElement | undefined;

  const [models, setModels] = createSignal<Record<string, string[]>>({});
  const [l2dLoaded, setL2DLoaded] = createSignal(false);

  const [selectedModel, setSelectedModel] = createSignal("airi0_home");
  const [scaleValue, setScaleValue] = createSignal(0.8);
  const [playVoice, setPlayVoice] = createSignal(false);
  const [voiceVolume, setVoiceVolume] = createSignal(1);
  const [tapToTalk, setTapToTalk] = createSignal(false);
  const [maxFPS, setMaxFPS] = createSignal(60);
  const [subtitle, setSubtitle] = createSignal<Subtitle>(Subtitle.none);

  onMount(() => {
    (window as any).wallpaperPropertyListener = {
      applyUserProperties: async function (properties: Record<string, any>) {
        if (properties.play_voice) {
          setPlayVoice(properties.play_voice.value);
          if (engine) engine.playVoice = properties.play_voice.value;
        }
        if (properties.tap_to_talk) {
          setTapToTalk(properties.tap_to_talk.value);
        }
        if (properties.voice_volume) {
          const vol = properties.voice_volume.value / 100;
          setVoiceVolume(vol);
          if (engine) engine.voiceVolume = vol;
        }
        if (properties.model) {
          const newModel = properties.model.value as string;
          if (selectedModel() !== newModel) {
            setSelectedModel(newModel);
          }
        }
        if (properties.scale) {
          setScaleValue(properties.scale.value);
          if (engine) engine.scale(properties.scale.value);
        }
        if (properties.subtitle) {
          setSubtitle(properties.subtitle.value);
        }
      },
      applyGeneralProperties: async function (properties: Record<string, any>) {
        if (properties.fps) {
          setMaxFPS(properties.fps.value);
          if (engine) (engine as any).app.ticker.maxFPS = properties.fps.value;
        }
      },
    };

    onCleanup(() => {
      delete (window as any).wallpaperPropertyListener;
      if (engine) {
        engine.destroy();
        engine = undefined;
      }
    });
  });

  onMount(() => {
    if (!canvasRef) return;
    engine = new Live2DWallpaperEngine(canvasRef);

    (async () => {
      const m = await fetchModels("./data/jp/Android/info.json");
      setModels(m);
    })();
  });

  createEffect(() => {
    const m = models();
    const sel = selectedModel();
    if (Object.keys(m).length === 0 || !engine) return;

    setL2DLoaded(false);

    (async () => {
      const model = m[sel];
      if (!model) return;

      for (let i = 0; i < model.length; i++) {
        const x = model[i];
        if (i === 0) await engine!.loadModel(x);
        else await engine!.addSpine(x, i.toString(), 0);
      }

      setL2DLoaded(true);
      engine!.center();
      engine!.scale(scaleValue());
      engine!.start();
    })();
  });

  createEffect(() => {
    if (!l2dLoaded() || !engine) return;

    const listener = {
      start: () => {
        const animation = engine!.currentAnimation;
        if (!animation || !subtitleRef) return;
        subtitleRef.innerHTML = "";
        if (subtitle() === Subtitle.none) return;
        const [, devName] = getLocalName(selectedModel());
        subtitleRef.classList.remove("opacity-0");
        subtitleRef.classList.add("opacity-100");
        showSubtitles(subtitleRef, animation, devName);
      },
      end: () => {
        if (!subtitleRef) return;
        subtitleRef.classList.remove("opacity-100");
        subtitleRef.classList.add("opacity-0");
        setTimeout(() => {
          if (subtitleRef) subtitleRef.innerHTML = "";
        }, 300);
      },
    };

    engine.setListener(listener);

    onCleanup(() => {
      if (engine) engine.clearListener();
    });
  });

  createEffect(() => {
    const sub = subtitle();
    if (sub === Subtitle.none) {
      if (subtitleRef) subtitleRef.innerHTML = "";
    } else {
      Table.initialize(sub);
    }
  });

  return (
    <div class="flex h-full w-full items-center justify-center">
      <canvas
        ref={(el) => { canvasRef = el!; }}
        id="canvas"
        onClick={() => {
          if (engine?.currentAnimation) return;
          if (!tapToTalk()) return;
          engine?.randomTalk();
        }}
      />
      <div
        class="fixed bottom-24 left-0 right-0 z-20 flex flex-col px-4 transition-all duration-300 sm:px-8 xl:px-96"
        ref={(el) => { subtitleRef = el!; }}
      />
    </div>
  );
}
