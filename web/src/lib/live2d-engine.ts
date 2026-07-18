// Required on top of the file to ensure PIXI and pixi-spine are loaded correctly
import "pixi-spine";

import { Spine } from "@esotericsoftware/spine-pixi";
import { Howl } from "howler";
import { Spine as PixiSpine } from "pixi-spine";
import * as PIXI from "pixi.js";

export interface EngineCallbacks {
  onMove?: (x: number, y: number) => void;
  onScaleChange?: (scale: number) => void;
}

export interface EngineOptions {
  playVoice?: boolean;
  voiceVolume?: number;
  loopAnimation?: boolean;
  callbacks?: EngineCallbacks;
}

export class Live2DEngine {
  private app: PIXI.Application;
  protected char?: Spine | PixiSpine;
  private howl?: Howl;
  private baseURL: string;
  protected playVoiceValue: boolean;
  protected voiceVolumeValue: number;
  protected loopAnimationValue: boolean;
  private devName?: string;
  private callbacks?: EngineCallbacks;

  private loadedAssets = new Map<string, boolean>();
  private spineLoadSemaphore: Promise<null> = Promise.resolve(null);

  private FILTER_MULTISAMPLE_DEFAULT = PIXI.MSAA_QUALITY.HIGH;
  private filterMultisampleRestored = PIXI.settings.FILTER_MULTISAMPLE;

  protected talkListener?: any;

  constructor(canvas: HTMLCanvasElement, options: EngineOptions = {}) {
    const {
      playVoice = false,
      voiceVolume = 1,
      loopAnimation = false,
      callbacks,
    } = options;

    this.playVoiceValue = playVoice;
    this.voiceVolumeValue = voiceVolume;
    this.loopAnimationValue = loopAnimation;
    this.callbacks = callbacks;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    this.app = new PIXI.Application({
      width: window.innerWidth,
      height: window.innerHeight,
      view: canvas,
    });

    this.baseURL = this.getBaseURL();

    this.configure();
  }

  private configure() {
    PIXI.settings.FILTER_MULTISAMPLE = PIXI.MSAA_QUALITY.HIGH;
  }

  private resetConfiguration() {
    PIXI.settings.FILTER_MULTISAMPLE = this.filterMultisampleRestored;
  }

  private getBaseURL() {
    if (window.location.origin !== "file://") return window.location.origin;

    const scriptElement = document.createElement("script");
    scriptElement.src = "dummy.js";
    const scriptUrl = scriptElement.src;
    return scriptUrl.substring(0, scriptUrl.lastIndexOf("/") + 1);
  }

  set playVoice(v: boolean) {
    this.playVoiceValue = v;
  }

  set voiceVolume(v: number) {
    this.voiceVolumeValue = v;
  }

  set loopAnimation(v: boolean) {
    this.loopAnimationValue = v;
    if (this.char) {
      this.char.state.tracks[0]!.loop = v;
    }
  }

  resizeCanvas(width: number, height: number, canvas: HTMLCanvasElement) {
    canvas.width = width;
    canvas.height = height;
    this.app.renderer.resize(width, height);
  }

  clearStage() {
    this.app.stage = new PIXI.Container();
    if (this.howl !== undefined) this.howl.stop();
  }

  async loadModel(src: string) {
    this.clearStage();

    const char = await this.addSpine(src, "char");
    this.char = char;

    this.devName = src
      .split("/")
      .pop()
      ?.split(".")[0]
      .split("_")
      .slice(0, -1)
      .join("_");

    const startAnimation = this.getAnimations().find(
      (a) => a.toLowerCase() === "start_idle_01",
    );
    if (startAnimation) {
      this.playAnimation(startAnimation);
    } else {
      const animation = char.state.data.skeletonData.animations[0];
      this.playAnimation(animation.name);
    }

    this.setupTalkListener(char);
  }

  private setupTalkListener(char: Spine | PixiSpine) {
    if (this.talkListener) {
      char.state.removeListener(this.talkListener);
      this.talkListener = undefined;
    }

    if (!this.playVoiceValue) return;

    this.talkListener = {
      event: async (entry: any, event: any) => {
        if (event.data.name !== "Talk") return;
        if (this.howl !== undefined) this.howl.stop();

        const characterId =
          this.devName || event.data.stringValue.split("_")[0];
        const fileName = (event.data.stringValue + ".ogg").toLowerCase();
        const host = this.getBaseURL();
        const src = `${host}/data/jp/MediaResources/GameData/Audio/VOC_JP/JP_${characterId}/${fileName}`;

        this.howl = new Howl({
          volume: this.voiceVolumeValue,
          src,
        });

        if (this.howl.state() === "loaded") {
          this.howl.play();
        } else {
          char.state.timeScale = 0;
          this.howl.on("load", () => {
            this.howl!.play();
            char.state.timeScale = 1;
          });
          this.howl.on("loaderror", () => {
            console.error("Failed to load voice line.");
            char.state.timeScale = 1;
          });
        }
      },
    };

    char.state.addListener(this.talkListener);
  }

  getScale(): number {
    const children = this.app.stage.children;
    for (const child of children) {
      if (child instanceof Spine || child instanceof PixiSpine) {
        return child.scale.x;
      }
    }
    return 1;
  }

  destroy() {
    if (this.char && this.talkListener) {
      this.char.state.removeListener(this.talkListener);
      this.talkListener = undefined;
    }

    if (this.howl) {
      this.howl.stop();
      this.howl.unload();
      this.howl = undefined;
    }

    for (const [key, _] of this.loadedAssets.entries()) {
      try {
        PIXI.Assets.unload(key);
      } catch (e) {
        console.warn(`Failed to unload asset ${key}`, e);
      }
    }
    this.loadedAssets.clear();

    if (this.app) {
      this.app.destroy(true);
      this.app = undefined as any;
    }

    this.char = undefined;
    this.resetConfiguration();
  }

  async addSpine(
    src: string,
    name: string,
    index?: number,
  ): Promise<Spine | PixiSpine> {
    return this.spineLoadSemaphore.then(async () => {
      const filename = src.split("/").pop()!.split(".").slice(0, -1).join(".");
      const skelKey = `${filename}Skel`;
      const atlasKey = `${filename}Atlas`;

      let spine: Spine | PixiSpine;

      const oldSkelParser = PIXI.Assets.loader.parsers.find(
        (p: any) => p.test && p.test("a.skel"),
      )!;
      const oldAtlasParser = PIXI.Assets.loader.parsers.find(
        (p: any) => p.test && p.test("a.atlas"),
      )!;

      try {
        PIXI.Assets.loader.parsers = PIXI.Assets.loader.parsers.filter(
          (p: any) => p !== oldSkelParser && p !== oldAtlasParser,
        );

        PIXI.Assets.add({
          alias: skelKey,
          src,
        });
        PIXI.Assets.add({
          alias: atlasKey,
          src: src.replace(".skel", ".atlas"),
        });
        await PIXI.Assets.load([skelKey, atlasKey]);
        spine = Spine.from(skelKey, atlasKey);

        PIXI.Assets.loader.reset();
        PIXI.Assets.loader.parsers.unshift(oldSkelParser, oldAtlasParser);
        console.log("spine version >= 4.2");
      } catch (_) {
        console.log("spine version < 4.2");

        PIXI.Assets.loader.reset();
        PIXI.Assets.loader.parsers.unshift(oldSkelParser, oldAtlasParser);

        PIXI.Assets.unload(skelKey);
        const data = await PIXI.Assets.load(src);
        spine = new PixiSpine(data.spineData);
      }

      this.loadedAssets.set(skelKey, true);
      this.loadedAssets.set(atlasKey, true);

      spine.name = name;

      if (index !== undefined) {
        this.app.stage.addChildAt(spine, index);
      } else {
        this.app.stage.addChild(spine);
      }

      const width =
        (spine instanceof PixiSpine ? spine.spineData.width : spine.width) || 0;
      const height =
        (spine instanceof PixiSpine ? spine.spineData.height : spine.height) ||
        0;

      const fillScale = this.calculateFillScale(width, height);
      const roundedScale = Math.ceil(fillScale * 10) / 10;

      spine.scale.set(roundedScale);

      return spine;
    });
  }

  private calculateFillScale(srcWidth: number, srcHeight: number): number {
    const widthScale = this.app.renderer.width / srcWidth;
    const heightScale = this.app.renderer.height / srcHeight;
    return Math.max(widthScale, heightScale);
  }

  resize(width?: number, height?: number) {
    const children = this.app.stage.children;
    children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      const scaleX = width ? child.width / width : child.scale.x;
      const scaleY = height ? child.height / height : child.scale.y;

      const roundedScaleX = Math.round(scaleX * 10) / 10;
      const roundedScaleY = Math.round(scaleY * 10) / 10;

      child.scale.set(roundedScaleX, roundedScaleY);
    });
  }

  fillScale(): number {
    let s = 0;
    this.app.stage.children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      const scale = this.calculateFillScale(
        (child instanceof PixiSpine ? child.spineData.width : child.width) || 0,
        (child instanceof PixiSpine ? child.spineData.height : child.height) ||
          0,
      );

      const roundedScale = Math.ceil(scale * 10) / 10;
      child.scale.set(roundedScale);
      s = roundedScale;
    });
    return s;
  }

  fitScale() {
    this.app.stage.children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      const srcWidth =
        (child instanceof PixiSpine ? child.spineData.width : child.width) || 0;
      const srcHeight =
        (child instanceof PixiSpine ? child.spineData.height : child.height) ||
        0;

      const fitScale = Math.min(
        this.app.renderer.width / srcWidth,
        this.app.renderer.height / srcHeight,
      );

      const roundedScale = Math.ceil(fitScale * 100) / 100;
      child.scale.set(roundedScale);
    });
  }

  scale(scale?: number) {
    const children = this.app.stage.children;
    children.forEach((child) => {
      const scaleX = scale ?? child.scale.x;
      const scaleY = scale ?? child.scale.y;

      const roundedScaleX = Math.round(scaleX * 10) / 10;
      const roundedScaleY = Math.round(scaleY * 10) / 10;

      child.scale.set(roundedScaleX, roundedScaleY);

      if (this.callbacks?.onScaleChange) {
        this.callbacks.onScaleChange(roundedScaleX);
      }
    });
  }

  move(x?: number, y?: number) {
    const children = this.app.stage.children;
    children.forEach((child) => {
      const x2 = x ?? child.x;
      const y2 = y ?? child.y;

      const roundedX = Math.round(x2);
      const roundedY = Math.round(y2);

      child.x = roundedX;
      child.y = roundedY;

      if (this.callbacks?.onMove) {
        this.callbacks.onMove(roundedX, roundedY);
      }
    });
  }

  center(): [number, number] {
    const children = this.app.stage.children;
    let [x, y] = [0, 0];
    children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      child.x = this.app.renderer.width / 2;
      const childHeight =
        (child instanceof PixiSpine ? child.spineData.height : child.height) ||
        0;
      const childScale = child.scale.y || 1;

      if (childHeight * childScale < this.app.renderer.height) {
        child.y = this.app.renderer.height - childHeight * childScale * 1.25;
      } else {
        child.y = this.app.renderer.height;
      }
      [x, y] = [child.x, child.y];
    });
    return [x, y];
  }

  playAnimation(name: string, options: { onComplete?: () => void } = {}) {
    if (!this.char) return;

    if (this.howl !== undefined) this.howl.stop();

    if (name.endsWith("_M")) {
      const action = name.slice(0, -2) + "_A";
      if (this.hasAnimation(action)) {
        this.char.state.setAnimation(2, action, this.loopAnimation);
      }
    } else {
      this.char.state.clearTrack(2);
    }

    if (!name.includes("Idle")) {
      if (this.hasAnimation("Idle_01")) {
        this.char.state.setAnimation(1, "Idle_01", true);
      }
    } else {
      this.char.state.clearTrack(1);
    }

    this.char.state.setAnimation(0, name, this.loopAnimation);
    this.char.state.addListener({ complete: options.onComplete });
  }

  hasAnimation(name: string): boolean {
    if (!this.char) return false;

    const animations = this.char.state.data.skeletonData.animations;
    const animation = animations.find((a) => a.name === name);
    return !!animation;
  }

  getAnimation(name: string) {
    if (!this.char) return;

    const animations = this.char.state.data.skeletonData.animations;
    const animation = animations.find((a) => a.name === name);
    return animation;
  }

  getAnimations(): string[] {
    if (!this.char) return [];

    const animations = this.char.state.data.skeletonData.animations;
    const names = animations.map((a) => a.name);
    return names;
  }
}
