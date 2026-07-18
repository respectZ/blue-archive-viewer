import { Live2DEngine } from "../live2d-engine";

export const exporter = async (
  engine: Live2DEngine,
  animationName: string,
  playVoice: boolean,
  loopAnimation: boolean,
  bitrate: number = 5,
  fps: number = 60,
  events?: { onPercentChange?: (percent: number) => void },
): Promise<string> => {
  const canvas = document.getElementById("canvas") as HTMLCanvasElement;
  const videoStream = canvas.captureStream(fps);
  const mediaOptions = {
    mimeType: "video/webm; codecs=vp9",
    videoBitsPerSecond: bitrate * 1024 * 1024,
  };
  const mediaRecorder = new MediaRecorder(videoStream, mediaOptions);
  const chunks: Blob[] = [];
  mediaRecorder.addEventListener("dataavailable", (e) => {
    chunks.push(e.data);
  });

  let r: string;
  mediaRecorder.addEventListener("stop", () => {
    const blob = new Blob(chunks, { type: "video/webm" });
    r = URL.createObjectURL(blob);
  });

  mediaRecorder.start();
  const voice = playVoice;
  const loop = loopAnimation;
  engine.playVoice = false;
  engine.loopAnimation = false;
  engine.playAnimation(animationName, {
    onComplete() {
      mediaRecorder.stop();
      engine.playVoice = voice;
      engine.loopAnimation = loop;
    },
  });

  const animData = engine.getAnimation(animationName);
  const duration = animData?.duration ?? 1;
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
