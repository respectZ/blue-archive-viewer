"use client";

import { Live2DViewer } from "@/app/lib/live2d_viewer";
import { localizeCharFromDevName } from "./character";
import { getBGMByDevName } from "./bgm";
import { getSubtitles } from "./subtitle";
import { toast } from "./toast";
import { exporter } from "./exporter";
import Modal from "@/app/component/modal";
import ProgressBar from "@/app/component/progress_bar";
import { createRoot } from "react-dom/client";

const __ver__ = "r61_ayufxz7uopaacimkmpwl"; // version: 1.37

export interface Elements {
  jsonData?: HTMLAnchorElement;
  settingPanel?: HTMLDivElement;
  subtitle?: HTMLDivElement;
  animationSelect?: HTMLSelectElement;
  modelSelect?: HTMLSelectElement;

  loopAnimation?: HTMLInputElement;
  playVoice?: HTMLInputElement;
  playBGM?: HTMLInputElement;

  scale?: HTMLInputElement;

  offsetX?: HTMLInputElement;
  offsetY?: HTMLInputElement;

  audioBGM?: HTMLAudioElement;

  exportBitrate?: HTMLInputElement;
  exportFPS?: HTMLInputElement;

  modal?: HTMLDivElement;
  progressBar?: HTMLDivElement;
  modalClose?: HTMLButtonElement;
}

export const CloseSetting = (element: HTMLDivElement) => {
  element.classList.add("-left-full");
  element.classList.remove("left-0");
};

export const OpenSetting = (element: HTMLDivElement) => {
  element.classList.add("left-0");
  element.classList.remove("-left-full");
};

export const PlayVoiceOnChanged = (v: boolean, live2d: Live2DViewer) => {
  live2d.playVoice = v;
};

/**
 * Called when model is changed to reload animation list.
 * @param selectElement - A select element.
 * @param v - A list of animation names.
 */
export const ReloadAnimations = (selectElement: HTMLSelectElement, v: string[]) => {
  selectElement.innerHTML = "";
  for (const animation of v) {
    const option = document.createElement("option");
    option.value = animation;
    option.innerText = animation;
    selectElement.appendChild(option);
    if (option.innerText === "Start_Idle_01") {
      option.selected = true;
    }
  }
};

/**
 * Reload model list.
 * @param selectElement - A select element.
 * @param v - A pair of model DevName and list of .skel files.
 */
export const ReloadModels = (selectElement: HTMLSelectElement, v: Record<string, string[]>, sort: boolean = true) => {
  if (sort) {
    // Compare by getLocalName(key)
    const sorted = Object.entries(v).sort((a, b) => {
      const [aLocalName, aDevName] = getLocalName(a[0]);
      const [bLocalName, bDevName] = getLocalName(b[0]);
      return aLocalName.localeCompare(bLocalName);
    });
    v = Object.fromEntries(sorted);
  }
  selectElement.innerHTML = "";
  let flag = false;
  for (const [model, files] of Object.entries(v)) {
    const option = document.createElement("option");
    const [localName, devName] = getLocalName(model);
    option.value = JSON.stringify(files);
    option.innerText = `${localName} (${model})`;
    option.setAttribute("data-devname", devName);
    selectElement.appendChild(option);
    if (!flag) {
      option.selected = true;
      flag = true;
    }
  }
};

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
      k = localizeCharFromDevName(`${devName.substring(0, devName.length - 1)}_default`);
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

export const AnimationOnChanged = (elements: Elements, live2d: Live2DViewer) => {
  const selectElement = elements.animationSelect!;
  const animation = selectElement.value;

  // Clear subtitles
  elements.subtitle!.innerHTML = "";

  live2d.playAnimation(animation);

  // Show subtitles
  showSubtitles(elements);
};

export const LoadModel = async (elements: Elements, live2d: Live2DViewer) => {
  const { modelSelect, animationSelect, offsetX, offsetY, scale } = elements;

  const files = JSON.parse(modelSelect!.value) as string[];
  let animations: string[] = [];
  animationSelect!.innerHTML = "";
  for (let i = 0; i < files.length; i++) {
    const file = files[i];

    if (i === 0) {
      await live2d.loadModel(file);
      animations = live2d.getAnimations();

      const char = live2d.char;
      if (char === undefined) continue;

      scale!.value = char.scale.x.toString();
    } else await live2d.addSpine(file, i.toString(), 0);
  }
  const [x, y] = live2d.center();
  offsetX!.value = x.toString();
  offsetY!.value = y.toString();
  // Clear subtitles
  elements.subtitle!.innerHTML = "";
  ReloadAnimations(animationSelect!, animations);
  ReloadBGM(elements);
};

export const ScaleChanged = (elements: Elements, live2d: Live2DViewer) => {
  const { scale } = elements;

  const s = parseFloat(scale!.value);

  live2d.scale(s);
};

export const OffsetChanged = (elements: Elements, live2d: Live2DViewer) => {
  const { offsetX, offsetY } = elements;

  const x = parseFloat(offsetX!.value);
  const y = parseFloat(offsetY!.value);

  live2d.move(x, y);
};

export const OffsetCenter = (elements: Elements, live2d: Live2DViewer) => {
  const [x, y] = live2d.center();

  elements.offsetX!.value = x.toString();
  elements.offsetY!.value = y.toString();
};

export const ScaleFill = (elements: Elements, live2d: Live2DViewer) => {
  const s = live2d.fillScale();
  elements.scale!.value = s.toString();
};

export const ScaleFit = (elements: Elements, live2d: Live2DViewer) => {
  const s = live2d.fitScale();
  elements.scale!.value = s.toString();
};

export const OnResize = (elements: Elements, live2d: Live2DViewer) => {
  console.log(`[Live2DViewer] Resize: ${window.innerWidth}x${window.innerHeight}`);
  live2d.resizeCanvas(window.innerWidth, window.innerHeight, document.getElementById("canvas")! as HTMLCanvasElement);
  // Re-center
  OffsetCenter(elements, live2d);
};

export const ReloadBGM = (elements: Elements) => {
  if (elements.playBGM === undefined) return;

  const { playBGM } = elements;
  const audio = elements.audioBGM! as HTMLAudioElement;
  if (playBGM.checked) {
    const selectedModel = elements.modelSelect!.selectedOptions[0];
    const devName = selectedModel.getAttribute("data-devname")!;
    const bgmId = getBGMByDevName(devName);
    // Pad with 0
    const bgmIdStr = bgmId.toString().padStart(2, "0");

    const bgmURL = `https://prod-clientpatch.bluearchiveyostar.com/${__ver__}/MediaResources/Audio/BGM/Theme_${bgmIdStr}.ogg`;
    audio.src = bgmURL;
    audio.hidden = false;
    audio.play().catch((e) => {
      toast(`Failed to play BGM: ${e}`);
      audio.hidden = true;
    });
  } else {
    // Reset audio
    audio.src = "";
    audio.hidden = true;
    audio.pause();
  }
};

const showSubtitles = (elements: Elements) => {
  // Get talkId and talkIndex
  const animationName = elements.animationSelect!.value;

  const devName = elements.modelSelect!.selectedOptions[0].getAttribute("data-devname")!;
  const subtitles = getSubtitles(animationName, { devName: devName });

  const subtitleElement = elements.subtitle!;
  subtitleElement.innerHTML = "";

  // Create subtitle element
  for (const subtitle of subtitles) {
    const p = document.createElement("p");
    p.innerText = subtitle;
    p.classList.add("text-xl", "text-gray-200", "mb-2", "p-2", "bg-neutral-800", "bg-opacity-80");
    subtitleElement.appendChild(p);
  }
};

let dragging = false;
let [charX, charY] = [0, 0];
let [mouseX, mouseY] = [0, 0];
let [initX, initY] = [0, 0];
export const EnableDragging = (elements: Elements, live2d: Live2DViewer) => {
  const canvas = document.getElementById("canvas")! as HTMLCanvasElement;

  canvas.onmousedown = (e) => {
    dragging = true;
    [charX, charY] = [-elements.offsetX!.valueAsNumber, -elements.offsetY!.valueAsNumber];
    [initX, initY] = [e.clientX - charX, e.clientY - charY];
  };

  canvas.onmouseup = () => {
    dragging = false;
  };

  canvas.onmouseout = () => {
    dragging = false;
  };

  canvas.onmousemove = (e) => {
    if (!dragging) return;

    [mouseX, mouseY] = [e.clientX - charX, e.clientY - charY];
    if (initX - mouseX != 0 || initY - mouseY != 0) {
      elements.offsetX!.value = (-(charX + initX - mouseX)).toString();
      elements.offsetY!.value = (-(charY + initY - mouseY)).toString();
      OffsetChanged(elements, live2d);
    }
  };
};

export const ExportAs = async (elements: Elements, live2d: Live2DViewer) => {
  const { exportBitrate, exportFPS, modal, progressBar, modalClose } = elements;

  const bitrate = exportBitrate!.valueAsNumber;
  const fps = exportFPS!.valueAsNumber;

  const video = modal?.querySelector("video")!;
  const title = modal?.querySelector("p")!;

  title.innerText = "Exporting...";
  modal?.classList.remove("hidden");
  modalClose?.classList.add("hidden");
  progressBar?.style.setProperty("width", "0%");
  video.src = "";

  const url = await exporter(elements, live2d, bitrate, fps, {
    onPercentChange(percent) {
      progressBar?.style.setProperty("width", `${percent}%`);
    },
  });

  title.innerText = "Exported!";
  modalClose?.classList.remove("hidden");
  video.src = url;
};
