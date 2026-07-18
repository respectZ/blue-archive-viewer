import {
  createSignal,
  onMount,
  onCleanup,
} from "solid-js";
import { Live2DEngine, EngineCallbacks, type EngineOptions } from "../lib/live2d-engine";

interface Live2DCanvasProps {
  id?: string;
  onEngineReady?: (engine: Live2DEngine) => void;
  onEngineCleanup?: () => void;
  onCanvasRef?: (canvas: HTMLCanvasElement) => void;
  playVoice?: boolean;
  voiceVolume?: number;
  loopAnimation?: boolean;
  onMove?: (x: number, y: number) => void;
  onScaleChange?: (scale: number) => void;
}

export function Live2DCanvas(props: Live2DCanvasProps) {
  const [engine, setEngine] = createSignal<Live2DEngine | null>(null);
  let canvasRef: HTMLCanvasElement | undefined;

  onMount(async () => {
    if (!canvasRef) return;

    const callbacks: EngineCallbacks = {
      onMove: props.onMove,
      onScaleChange: props.onScaleChange,
    };

    const engineInstance = new Live2DEngine(canvasRef, {
      playVoice: props.playVoice,
      voiceVolume: props.voiceVolume,
      loopAnimation: props.loopAnimation,
      callbacks,
    });

    setEngine(engineInstance);
    props.onEngineReady?.(engineInstance);
  });

  onCleanup(() => {
    const e = engine();
    if (e) {
      e.destroy();
      setEngine(null);
      props.onEngineCleanup?.();
    }
  });

  return (
    <canvas
      id={props.id}
      ref={el => {
        canvasRef = el!;
        canvasRef.width = window.innerWidth;
        canvasRef.height = window.innerHeight;
        props.onCanvasRef?.(canvasRef!);
      }}
      class="w-full h-full block touch-none"
      style="display: block;"
    />
  );
}