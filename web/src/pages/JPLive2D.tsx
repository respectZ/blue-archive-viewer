import { createSignal, For, Show, onMount, onCleanup } from "solid-js";
import { Live2DCanvas } from "../components/Live2DCanvas";
import { Live2DEngine } from "../lib/live2d-engine";
import { InputCheckbox } from "../components/InputCheckbox";
import { InputNumber } from "../components/InputNumber";
import { Button } from "../components/Button";
import { Accordion } from "../components/Accordion";
import { Modal } from "../components/Modal";
import { ProgressBar } from "../components/ProgressBar";
import * as Table from "../lib/table";
import { get_origin } from "../lib/get_origin";
import { fetchModels } from "../lib/live2d/model";
import {
  buildModelOptions,
  getModelBGMUrl,
  downloadAsWallpaperEngine,
  type ModelOption,
} from "../lib/live2d/events";
import { getSubtitles } from "../lib/live2d/subtitle";
import { toast } from "../lib/live2d/toast";
import { exporter } from "../lib/live2d/exporter";

type Changelog = {
  versions: {
    version: string;
    date: string;
    changelogs: Record<string, string[]>;
  }[];
};

export function JPLive2D() {
  const region = "jp" as const;

  let engine: Live2DEngine | undefined;
  let canvasEl: HTMLCanvasElement | undefined;
  let audioRef: HTMLAudioElement | undefined;
  let subtitleRef: HTMLDivElement | undefined;
  let progressBarRef: HTMLDivElement | undefined;

  const [loading, setLoading] = createSignal(true);
  const [settingsOpen, setSettingsOpen] = createSignal(false);
  const [modelOptions, setModelOptions] = createSignal<ModelOption[]>([]);
  const [selectedModelValue, setSelectedModelValue] = createSignal("");
  const modelMetadata = new Map<string, { devName: string; model: string }>();

  const [animations, setAnimations] = createSignal<string[]>([]);
  const [selectedAnimation, setSelectedAnimation] = createSignal("");

  const [loopAnimation, setLoopAnimation] = createSignal(false);
  const [playVoice, setPlayVoice] = createSignal(false);
  const [playBGM, setPlayBGM] = createSignal(false);

  const [scaleValue, setScaleValue] = createSignal(1);
  const [offsetXValue, setOffsetXValue] = createSignal(0);
  const [offsetYValue, setOffsetYValue] = createSignal(0);

  const [exportBitrate, setExportBitrate] = createSignal(5);
  const [exportFPS, setExportFPS] = createSignal(30);

  const [exporting, setExporting] = createSignal(false);
  const [exportProgress, setExportProgress] = createSignal(0);
  const [videoUrl, setVideoUrl] = createSignal("");

  const [changelog, setChangelog] = createSignal<Changelog>();
  const [subtitles, setSubtitles] = createSignal<string[]>([]);

  const [modalRef, setModalRef] = createSignal<HTMLDivElement | undefined>();

  let dragging = false;
  let charX = 0,
    charY = 0;
  let initX = 0,
    initY = 0;
  let mouseX = 0,
    mouseY = 0;
  let pinchStartDistance = 0;
  let pinchZooming = false;

  const getDistance = (t1: Touch, t2: Touch) => {
    const dx = t1.clientX - t2.clientX;
    const dy = t1.clientY - t2.clientY;
    return Math.sqrt(dx * dx + dy * dy);
  };

  const setupCanvasDrag = (canvas: HTMLCanvasElement) => {
    canvas.onpointerdown = (e) => {
      if (pinchZooming) return;
      dragging = true;
      charX = -offsetXValue();
      charY = -offsetYValue();
      initX = e.clientX - charX;
      initY = e.clientY - charY;
    };
    canvas.onpointerup = () => {
      dragging = false;
    };
    canvas.onpointerout = () => {
      dragging = false;
    };
    canvas.onpointermove = (e) => {
      if (pinchZooming || !dragging || !engine) return;
      mouseX = e.clientX - charX;
      mouseY = e.clientY - charY;
      if (initX - mouseX !== 0 || initY - mouseY !== 0) {
        const newX = -(charX + initX - mouseX);
        const newY = -(charY + initY - mouseY);
        setOffsetXValue(newX);
        setOffsetYValue(newY);
        engine.move(newX, newY);
      }
    };
    canvas.addEventListener("touchstart", (e) => {
      if (e.touches.length === 2) {
        pinchStartDistance = getDistance(e.touches[0], e.touches[1]);
        pinchZooming = true;
      }
    });
    canvas.addEventListener("touchend", () => {
      pinchZooming = false;
    });
    canvas.addEventListener("touchmove", (e) => {
      if (pinchZooming && e.touches.length === 2 && engine) {
        const currentDistance = getDistance(e.touches[0], e.touches[1]);
        const pinchDelta = currentDistance - pinchStartDistance;
        if (pinchDelta !== 0) {
          const v = scaleValue() + pinchDelta / 2000;
          if (v >= 0.1 && v <= 20) {
            setScaleValue(v);
            engine.scale(v);
          }
        }
        pinchStartDistance = currentDistance;
      }
    });
    canvas.onclick = () => {
      setSettingsOpen(false);
    };
  };

  const reloadBGM = () => {
    if (!audioRef) return;
    if (playBGM()) {
      const sel = modelOptions().find((o) => o.value === selectedModelValue());
      if (!sel) return;
      const url = getModelBGMUrl(sel.devName);
      if (url) {
        audioRef.src = url;
        audioRef.hidden = false;
        audioRef.play().catch((e) => {
          toast(`Failed to play BGM: ${e}`);
          if (audioRef) audioRef.hidden = true;
        });
      }
    } else {
      audioRef.src = "";
      audioRef.hidden = true;
      audioRef.pause();
    }
  };

  const loadModel = async (value: string) => {
    if (!engine) return;
    const files = JSON.parse(value) as string[];
    let anims: string[] = [];
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      if (i === 0) {
        await engine.loadModel(file);
        anims = engine.getAnimations();
      } else {
        await engine.addSpine(file, i.toString(), 0);
      }
    }
    const [cx, cy] = engine.center();
    setAnimations(anims);
    setScaleValue(engine.getScale());
    setOffsetXValue(cx);
    setOffsetYValue(cy);
    setSubtitles([]);
    if (anims.length > 0) setSelectedAnimation(anims[0]);

    const idle = anims.find((a) => a.toLowerCase() === "start_idle_01");
    if (idle) setSelectedAnimation(idle);

    reloadBGM();
  };

  const handleAnimationChange = (value: string) => {
    if (!engine) return;
    setSelectedAnimation(value);
    setSubtitles([]);
    engine.playAnimation(value);
    const sel = modelOptions().find((o) => o.value === selectedModelValue());
    if (sel) {
      const subs = getSubtitles(value, { devName: sel.devName });
      setSubtitles(subs);
    }
  };

  const handleScaleChange = (value: number) => {
    if (!engine) return;
    setScaleValue(value);
    engine.scale(value);
  };

  const handleOffsetXChange = (value: number) => {
    if (!engine) return;
    setOffsetXValue(value);
    engine.move(value, offsetYValue());
  };

  const handleOffsetYChange = (value: number) => {
    if (!engine) return;
    setOffsetYValue(value);
    engine.move(offsetXValue(), value);
  };

  const handleScaleFill = () => {
    if (!engine) return;
    const s = engine.fillScale();
    setScaleValue(s);
  };

  const handleScaleFit = () => {
    if (!engine) return;
    engine.fitScale();
    setScaleValue(engine.getScale());
  };

  const handleOffsetCenter = () => {
    if (!engine) return;
    const [cx, cy] = engine.center();
    setOffsetXValue(cx);
    setOffsetYValue(cy);
  };

  const handleExport = async () => {
    if (!engine) return;
    setExporting(true);
    setExportProgress(0);
    setVideoUrl("");

    try {
      const url = await exporter(
        engine,
        selectedAnimation(),
        playVoice(),
        loopAnimation(),
        exportBitrate(),
        exportFPS(),
        {
          onPercentChange(pct) {
            setExportProgress(pct);
            if (progressBarRef) {
              progressBarRef.style.setProperty("width", `${pct}%`);
            }
          },
        },
      );
      setVideoUrl(url);
    } finally {
      setExporting(false);
    }
  };

  const handleModelChange = (value: string) => {
    setSelectedModelValue(value);
    loadModel(value);
  };

  onMount(async () => {
    console.warn("ok");
    await Table.initialize(region);

    const origin = get_origin();
    const models = await fetchModels(`${origin}/data/jp/Android/info.json`);
    for (const [key, value] of Object.entries(models)) {
      models[key] = value.map((v) => origin + "/" + v);
    }
    const opts = buildModelOptions(models, false);
    opts.forEach((o) =>
      modelMetadata.set(o.value, { devName: o.devName, model: o.model }),
    );
    setModelOptions(opts);
    if (opts.length > 0) {
      setSelectedModelValue(opts[0].value);
    }

    if (region === "jp") {
      fetch(`${origin}/data/${region}/changelog.json`)
        .then((r) => r.json())
        .then((d: Changelog) => setChangelog(d))
        .catch(() => {});
    }
  });

  onMount(() => {
    const check = setInterval(() => {
      if (engine && modelOptions().length > 0 && selectedModelValue()) {
        clearInterval(check);
        setLoading(false);
        loadModel(selectedModelValue());
      }
    }, 50);
    onCleanup(() => clearInterval(check));
  });

  onMount(() => {
    const handleResize = () => {
      if (!engine || !canvasEl) return;
      const isMobile =
        /iPhone|iPad|iPod|Android|webOS|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent,
        );
      if (isMobile) return;
      console.log(
        `[Live2DEngine] Resize: ${window.innerWidth}x${window.innerHeight}`,
      );
      engine.resizeCanvas(window.innerWidth, window.innerHeight, canvasEl);
      handleOffsetCenter();
    };
    window.addEventListener("resize", handleResize);
    onCleanup(() => window.removeEventListener("resize", handleResize));
  });

  const animationOptions = () =>
    animations().map((a) => ({ value: a, label: a }));

  return (
    <main class="relative h-full w-full">
      <Modal
        ref={setModalRef}
        class={exporting() || videoUrl() ? "" : "hidden"}
      >
        <div class="flex w-full flex-col xl:w-96">
          <p class="mb-4 text-2xl font-semibold text-[var(--text-primary)]">
            {videoUrl() ? "Exported!" : "Exporting..."}
          </p>
          <Show when={!videoUrl()}>
            <ProgressBar
              class="mb-4 grow"
              height={2}
              percent={exportProgress()}
              ref={(el) => {
                progressBarRef = el;
              }}
            />
          </Show>
          <Show when={videoUrl()}>
            <video controls class="mb-4 rounded-lg" src={videoUrl()} />
          </Show>
          <Show when={videoUrl()}>
            <Button
              id="modal-close"
              label="Close"
              onClick={() => {
                setVideoUrl("");
                setExportProgress(0);
                const m = modalRef();
                if (m) m.classList.add("hidden");
              }}
            />
          </Show>
        </div>
      </Modal>

      <Show when={loading()}>
        <div class="fixed inset-0 z-50 flex items-center justify-center bg-[var(--bg-base)]/90 backdrop-blur transition-all duration-1000">
          <div class="relative flex flex-col items-center gap-4">
            <div class="h-12 w-12 animate-spin rounded-full border-2 border-[var(--border)] border-t-[var(--accent)] shadow-[0_0_16px_var(--accent-glow)]" />
            <p class="text-lg font-medium text-[var(--text-secondary)]">
              Loading...
            </p>
          </div>
        </div>
      </Show>

      <button
        id="setting-button"
        class="fixed left-4 top-4 z-30 flex h-11 w-11 items-center justify-center rounded-full border border-[var(--border)] bg-[var(--surface)]/80 text-[var(--text-primary)] shadow-lg backdrop-blur transition-all hover:border-[var(--accent)] hover:text-[var(--accent)] hover:shadow-[0_0_20px_var(--accent-glow)]"
        onClick={() => setSettingsOpen(true)}
      >
        <svg
          width="20"
          height="20"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
          class="text-current"
        >
          <circle
            fill="none"
            stroke="currentColor"
            cx="9.997"
            cy="10"
            r="3.31"
          />
          <path
            fill="none"
            stroke="currentColor"
            d="M18.488,12.285 L16.205,16.237 C15.322,15.496 14.185,15.281 13.303,15.791 C12.428,16.289 12.047,17.373 12.246,18.5 L7.735,18.5 C7.938,17.374 7.553,16.299 6.684,15.791 C5.801,15.27 4.655,15.492 3.773,16.237 L1.5,12.285 C2.573,11.871 3.317,10.999 3.317,9.991 C3.305,8.98 2.573,8.121 1.5,7.716 L3.765,3.784 C4.645,4.516 5.794,4.738 6.687,4.232 C7.555,3.722 7.939,2.637 7.735,1.5 L12.263,1.5 C12.072,2.637 12.441,3.71 13.314,4.22 C14.206,4.73 15.343,4.516 16.225,3.794 L18.487,7.714 C17.404,8.117 16.661,8.988 16.67,10.009 C16.672,11.018 17.415,11.88 18.488,12.285 Z"
          />
        </svg>
      </button>

      <div
        classList={{
          "fixed top-0 left-0 z-40 h-full w-full xl:w-96 overflow-y-auto border-r border-[var(--border)] bg-[var(--surface)]/95 p-6 shadow-2xl backdrop-blur-xl transition-transform duration-300": true,
          "-translate-x-full": !settingsOpen(),
          "translate-x-0": settingsOpen(),
        }}
        id="setting"
      >
        <div class="flex flex-row justify-end text-[var(--text-primary)]">
          <svg
            id="close"
            width="16"
            height="16"
            viewBox="0 0 14 14"
            xmlns="http://www.w3.org/2000/svg"
            class="cursor-pointer text-[var(--text-secondary)] transition-colors hover:text-[var(--accent)]"
            onClick={() => setSettingsOpen(false)}
          >
            <line
              fill="none"
              stroke="currentColor"
              stroke-width="1.1"
              x1="1"
              y1="1"
              x2="13"
              y2="13"
            />
            <line
              fill="none"
              stroke="currentColor"
              stroke-width="1.1"
              x1="13"
              y1="1"
              x2="1"
              y2="13"
            />
          </svg>
        </div>

        <div class="flex flex-col gap-6 pb-12 pt-4">
          <p class="text-2xl font-bold text-[var(--text-primary)]">Settings</p>

          <div class="flex flex-col gap-1">
            <label
              for="model"
              class="text-sm font-medium text-[var(--text-secondary)]"
            >
              Model
            </label>
            <select
              id="model"
              class="h-10 w-full rounded-lg border border-[var(--border)] bg-[var(--bg-base)] px-3 text-sm text-[var(--text-primary)] transition focus:border-[var(--accent)] focus:outline-none focus:ring-2 focus:ring-[var(--accent)]/30"
              onChange={(e) => {
                const val = (e.currentTarget as HTMLSelectElement).value;
                handleModelChange(val);
              }}
            >
              <For each={modelOptions()}>
                {(opt) => (
                  <option
                    value={opt.value}
                    selected={opt.value === selectedModelValue()}
                  >
                    {opt.label}
                  </option>
                )}
              </For>
            </select>
          </div>

          <div class="flex flex-col gap-1">
            <label
              for="animation"
              class="text-sm font-medium text-[var(--text-secondary)]"
            >
              Animation
            </label>
            <select
              id="animation"
              class="h-10 w-full rounded-lg border border-[var(--border)] bg-[var(--bg-base)] px-3 text-sm text-[var(--text-primary)] transition focus:border-[var(--accent)] focus:outline-none focus:ring-2 focus:ring-[var(--accent)]/30"
              onChange={(e) => {
                handleAnimationChange(
                  (e.currentTarget as HTMLSelectElement).value,
                );
              }}
            >
              <For each={animationOptions()}>
                {(opt) => (
                  <option
                    value={opt.value}
                    selected={opt.value === selectedAnimation()}
                  >
                    {opt.label}
                  </option>
                )}
              </For>
            </select>
          </div>

          <div class="flex flex-col gap-4 rounded-xl border border-[var(--border)] bg-[var(--bg-elevated)] p-4">
            <InputCheckbox
              id="loop-animation"
              label="Loop animation"
              defaultChecked={loopAnimation()}
              onChange={(v) => {
                setLoopAnimation(v);
                if (engine) engine.loopAnimation = v;
              }}
            />
            <InputCheckbox
              id="play-voice"
              label="Play voice"
              defaultChecked={playVoice()}
              onChange={(v) => {
                setPlayVoice(v);
                if (engine) engine.playVoice = v;
              }}
            />
            <InputCheckbox
              id="play-bgm"
              label="Play BGM"
              defaultChecked={playBGM()}
              onChange={(v) => {
                setPlayBGM(v);
                reloadBGM();
              }}
            />
          </div>

          <audio
            src=""
            preload="auto"
            ref={(el) => {
              audioRef = el;
            }}
            loop
            controls
            hidden
          />

          <Button
            id="download"
            label="Download as Wallpaper Engine Web"
            onClick={() => {
              const sel = modelOptions().find(
                (o) => o.value === selectedModelValue(),
              );
              if (sel) downloadAsWallpaperEngine(sel.model);
            }}
          />

          <Accordion title="Extras">
            <div class="flex flex-col gap-4">
              <div>
                <p class="mb-2 text-sm font-medium text-[var(--text-secondary)]">
                  Scale
                </p>
                <div class="flex flex-wrap gap-2">
                  <Button
                    id="scale-fill"
                    label="Fill"
                    onClick={handleScaleFill}
                  />
                  <Button id="scale-fit" label="Fit" onClick={handleScaleFit} />
                </div>
              </div>
              <InputNumber
                id="scale-x"
                label="X"
                defaultValue={scaleValue()}
                min={0.1}
                max={20}
                step={0.1}
                onChange={(v) => handleScaleChange(v)}
              />
              <div>
                <p class="mb-2 text-sm font-medium text-[var(--text-secondary)]">
                  Offset
                </p>
                <div class="flex flex-wrap gap-2">
                  <Button
                    id="offset-center"
                    label="Center"
                    onClick={handleOffsetCenter}
                  />
                </div>
                <p class="text-sm text-[var(--text-muted)]">
                  You can also move by dragging it.
                </p>
              </div>
              <InputNumber
                id="offset-x"
                label="X"
                defaultValue={offsetXValue()}
                min={-1920}
                max={1920}
                step={1}
                onChange={(v) => handleOffsetXChange(v)}
              />
              <InputNumber
                id="offset-y"
                label="Y"
                defaultValue={offsetYValue()}
                min={-1080}
                max={1080}
                step={1}
                onChange={(v) => handleOffsetYChange(v)}
              />
            </div>
          </Accordion>

          <Accordion title="Export">
            <div class="flex flex-col gap-4">
              <InputNumber
                id="export-bitrate"
                label="Bitrate (Mbps)"
                defaultValue={exportBitrate()}
                min={5}
                max={100}
                step={1}
                onChange={(v) => setExportBitrate(v)}
              />
              <InputNumber
                id="export-fps"
                label="FPS"
                defaultValue={exportFPS()}
                min={1}
                max={60}
                step={1}
                onChange={(v) => setExportFPS(v)}
              />
              <Button id="export-button" label="Go!" onClick={handleExport} />
            </div>
          </Accordion>

          <Accordion title="Changelog">
            <div class="text-sm text-[var(--text-secondary)]">
              <Show when={changelog()?.versions[0]}>
                {(() => {
                  const c = changelog()!;
                  const { version, date, changelogs: logs } = c.versions[0];
                  const live2dEntries = logs.live2d;
                  return (
                    <>
                      <h2 class="mb-1 text-lg font-semibold text-[var(--text-primary)]">
                        {version}
                      </h2>
                      <p class="mb-3">{new Date(date).toLocaleDateString()}</p>
                      <Show when={live2dEntries}>
                        <ul class="list-disc pl-5">
                          <For each={live2dEntries}>
                            {(entry) => (
                              <li class="mb-1">
                                <p class="break-keep">- {entry}</p>
                              </li>
                            )}
                          </For>
                        </ul>
                      </Show>
                    </>
                  );
                })()}
              </Show>
            </div>
          </Accordion>
        </div>
      </div>

      <div class="flex h-full w-full items-center justify-center">
        <Live2DCanvas
          id="canvas"
          onEngineReady={(eng) => {
            engine = eng;
          }}
          onCanvasRef={(canvas) => {
            canvasEl = canvas;
            setupCanvasDrag(canvas);
          }}
        />
      </div>

      <div class="fixed bottom-0 left-0 right-0 z-20 flex h-12 items-center justify-center border-t border-[var(--border)] bg-[var(--surface)]/80 text-sm text-[var(--text-muted)] backdrop-blur">
        Live2D Viewer
      </div>

      <div
        class="fixed bottom-20 left-0 right-0 z-20 flex flex-col px-4 sm:px-8 xl:px-96"
        ref={(el) => {
          subtitleRef = el;
        }}
      >
        <For each={subtitles()}>
          {(sub) => (
            <p class="mb-2 rounded-lg border border-[var(--border)] bg-[var(--bg-base)]/80 p-2 text-lg text-[var(--text-primary)] backdrop-blur">
              {sub}
            </p>
          )}
        </For>
      </div>
    </main>
  );
}
