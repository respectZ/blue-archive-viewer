import { Live2DViewer } from "@/app/lib/live2d_viewer";
import { Elements } from "./events";

export const exporter = async (elements: Elements, live2d: Live2DViewer, bitrate: number = 5, fps: number = 60, events?: { onPercentChange?: (percent: number) => void }) => {
  let r: string;
  const canvas = document.getElementById("canvas")! as HTMLCanvasElement;
  const videoStream = canvas.captureStream(fps);
  const mediaOptions = { mimeType: "video/webm; codecs=vp9", videoBitsPerSecond: bitrate * 1024 * 1024 };
  const mediaRecorder = new MediaRecorder(videoStream, mediaOptions);

  const chunks: Blob[] = [];
  mediaRecorder.addEventListener("dataavailable", (e) => {
    chunks.push(e.data);
  });

  mediaRecorder.addEventListener("stop", () => {
    const blob = new Blob(chunks, { type: "video/webm" });
    const url = URL.createObjectURL(blob);
    r = url;
  });

  mediaRecorder.start();
  const voice = elements.playVoice!.checked;
  const loop = elements.loopAnimation!.checked;
  live2d.playVoice = false; // Reenable after recording
  live2d.loopAnimation = false; // Reenable after recording
  live2d.playAnimation(elements.animationSelect!.value, {
    onComplete() {
      mediaRecorder.stop();
      live2d.playVoice = voice;
      live2d.loopAnimation = loop;
    },
  });

  const animData = live2d.getAnimation(elements.animationSelect!.value)!;
  const duration = animData.duration;
  let progress = 0;

  return new Promise<string>((resolve) => {
    const interval = setInterval(() => {
      if (events?.onPercentChange) {
        progress++;
        events.onPercentChange(progress);
      }

      if (r) {
        clearInterval(interval);
        resolve(r);
      }
    }, duration * 10);
  });
};
