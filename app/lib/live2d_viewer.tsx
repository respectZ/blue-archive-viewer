import "pixi-spine";

import { Spine } from "@esotericsoftware/spine-pixi";
import { Howl } from "howler";
import { Spine as PixiSpine } from "pixi-spine";
import * as PIXI from "pixi.js";
import { AddressablesCatalogUrlRoot } from "../jp/url";
import { get_origin } from "./get_origin";

function calculateFitScale(
  srcWidth: number,
  srcHeight: number,
  maxWidth: number,
  maxHeight: number
) {
  const widthScale = maxWidth / srcWidth;
  const heightScale = maxHeight / srcHeight;

  // Use the smaller of the two scales to ensure the entire image fits within the canvas
  const fitScale = Math.min(widthScale, heightScale);

  return fitScale;
}

function calculateFillScale(
  srcWidth: number,
  srcHeight: number,
  maxWidth: number,
  maxHeight: number
) {
  const widthScale = maxWidth / srcWidth;
  const heightScale = maxHeight / srcHeight;

  // Use the larger of the two scales to ensure the canvas is completely filled by the image
  const fitScale = Math.max(widthScale, heightScale);

  return fitScale;
}

interface EventData {
  floatValue: number;
  intValue: number;
  stringValue: string;
  time: number;
}

export class Live2DViewer {
  app: PIXI.Application;
  char?: Spine | PixiSpine;

  playVoice: boolean = false;
  voiceVolume: number = 1;
  howl?: Howl;
  baseURL: string = AddressablesCatalogUrlRoot;
  private _loopAnimation: boolean = false;
  private devName?: string;

  constructor(canvas: HTMLCanvasElement) {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    this.app = new PIXI.Application({
      width: window.innerWidth,
      height: window.innerHeight,
      view: canvas,
    });
  }

  resizeCanvas(width: number, height: number, canvas: HTMLCanvasElement) {
    canvas.width = width;
    canvas.height = height;
    this.app.renderer.resize(width, height);
  }

  /**
   * Load a Live2D Model.
   * This method also clears the stage.
   * @param {string} src - Path to .skel file.
   * @example
   * const canvas = document.querySelector("canvas")!;
   * const l2d = new Live2DViewer(canvas);
   * l2d.loadModel("data/Android/airi_home/Airi_home.skel");
   */
  async loadModel(src: string) {
    // Clear stage
    this.clearStage();

    const char = await this.addSpine(src, "char");
    this.char = char;
    // /aru_newyear_home/Aru_newyear_home.skel => Aru_newyear_home
    this.devName = src
      .split("/")
      .pop()
      ?.split(".")[0]
      .split("_")
      .slice(0, -1)
      .join("_");

    // Play default animation
    // Ignore case
    const startAnimation = this.getAnimations().find(
      (a) => a.toLowerCase() === "start_idle_01"
    );
    if (startAnimation) {
      this.playAnimation(startAnimation);
    } else {
      const animation = char.state.data.skeletonData.animations[0];
      this.playAnimation(animation.name);
    }

    char.state.addListener({
      event: async (entry, event) => {
        if (!this.playVoice) return;
        if (event.data.name !== "Talk") return;

        if (this.howl !== undefined) this.howl.stop();

        const data = event as any as EventData;

        let fileName = (data.stringValue + ".ogg").toLowerCase();
        const characterId = this.devName || fileName.split("_")[0];
        const host = get_origin();
        const src = `${host}/data/jp/MediaResources/GameData/Audio/VOC_JP/JP_${characterId}/${fileName}`;

        this.howl = new Howl({
          volume: this.voiceVolume,
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
    });
  }

  /**
   * Clear a PIXI stage.
   */
  clearStage() {
    this.app.stage = new PIXI.Container();
    if (this.howl !== undefined) this.howl.stop();
  }

  /**
   * Add a spine to the stage.
   * @param {string} src - Path to .skel file
   * @param {string} name - A unique name
   * @param {number} index - Index to insert at
   * @returns {Promise<Spine | PixiSpine>}
   * @example
   * const live2d = new Live2DViewer(...);
   * live2d.addSpine("data/akari_home/akari_bg.skel", "bg", 0);
   */
  async addSpine(
    src: string,
    name: string,
    index?: number
  ): Promise<Spine | PixiSpine> {
    const filename = src.split("/").pop()!.split(".").slice(0, -1).join(".");
    const skelKey = `${filename}Skel`;
    const atlasKey = `${filename}Atlas`;

    let spine: Spine | PixiSpine;

    const oldSkelParser = PIXI.Assets.loader.parsers.find(
      (p) => p.test && p.test("a.skel")
    )!;
    const oldAtlasParser = PIXI.Assets.loader.parsers.find(
      (p) => p.test && p.test("a.atlas")
    )!;

    try {
      PIXI.Assets.loader.parsers = PIXI.Assets.loader.parsers.filter(
        (p) => p !== oldSkelParser && p !== oldAtlasParser
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
    } catch (_) {
      console.log("spine version < 4.2");

      PIXI.Assets.loader.reset();
      PIXI.Assets.loader.parsers.unshift(oldSkelParser, oldAtlasParser);

      PIXI.Assets.unload(skelKey);
      const data = await PIXI.Assets.load(src);
      spine = new PixiSpine(data.spineData);
    }
    spine.name = name;

    if (index !== undefined) {
      this.app.stage.addChildAt(spine, index);
    } else {
      this.app.stage.addChild(spine);
    }

    const width =
      (spine instanceof PixiSpine ? spine.spineData.width : spine.width) || 0;
    const height =
      (spine instanceof PixiSpine ? spine.spineData.height : spine.height) || 0;

    let scale = calculateFillScale(
      width,
      height,
      this.app.renderer.width,
      this.app.renderer.height
    );

    scale = Math.ceil(scale * 10) / 10;

    spine.scale.set(scale);

    return spine;
  }

  /**
   * Resize entire loaded assets.
   * @param width
   * @param height
   */
  resize(width?: number, height?: number) {
    const children = this.app.stage.children;
    children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      let scaleX = width ? child.width / width : child.scale.x;
      let scaleY = height ? child.height / height : child.scale.y;

      scaleX = Math.round(scaleX * 10) / 10;
      scaleY = Math.round(scaleY * 10) / 10;

      child.scale.set(scaleX, scaleY);
    });
  }

  /**
   * Fill scale entire loaded assets.
   */
  fillScale(): number {
    let s = 0;
    this.app.stage.children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      let scale = calculateFillScale(
        child.width,
        child.height,
        this.app.renderer.width,
        this.app.renderer.height
      );

      scale = Math.ceil(scale * 10) / 10;

      child.scale.set(scale);
      s = scale;
    });
    return s;
  }

  /**
   * Fit scale entire loaded assets.
   */
  fitScale() {
    let s = 0;
    this.app.stage.children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      let scale = calculateFitScale(
        child.width,
        child.height,
        this.app.renderer.width,
        this.app.renderer.height
      );

      scale = Math.ceil(scale * 100) / 100;

      child.scale.set(scale);
      s = scale;
    });
    return s;
  }

  /**
   * Scale entire loaded assets.
   * @param x
   * @param y
   * @example
   * const live2d = new Live2DViewer(...);
   * live2d.scale(1.5);
   * // Scale to 1.5x
   */
  scale(scale?: number) {
    const children = this.app.stage.children;
    children.forEach((child) => {
      let scaleX = scale ?? child.scale.x;
      let scaleY = scale ?? child.scale.y;

      scaleX = Math.round(scaleX * 10) / 10;
      scaleY = Math.round(scaleY * 10) / 10;

      child.scale.set(scaleX, scaleY);
    });
  }

  /**
   * Move offset of entire loaded assets.
   * @param x
   * @param y
   */
  move(x?: number, y?: number) {
    const children = this.app.stage.children;
    children.forEach((child) => {
      let x2 = x! ?? child.x;
      let y2 = y! ?? child.y;

      x2 = Math.round(x2);
      y2 = Math.round(y2);

      child.x = x2;
      child.y = y2;
    });
  }

  /**
   * Center entire loaded assets.
   * @returns {[number, number]} - [x, y]
   */
  center(): [number, number] {
    const children = this.app.stage.children;
    let [x, y] = [0, 0];
    children.forEach((child) => {
      if (!(child instanceof Spine || child instanceof PixiSpine)) return;

      child.x = this.app.renderer.width / 2;
      if (child.height * child.scale.y < this.app.renderer.height) {
        child.y =
          this.app.renderer.height - child.height * child.scale.y * 1.25;
      } else {
        child.y = this.app.renderer.height;
      }
      [x, y] = [child.x, child.y];
    });
    return [x, y];
  }

  /**
   * Play a char animation.
   * @param name
   */
  playAnimation(name: string, options: { onComplete?: () => void } = {}) {
    if (!this.char) return;

    if (this.howl !== undefined) this.howl.stop();

    // If last animation name is M, play M (mouth/music?) + A (action?)
    if (name.endsWith("_M")) {
      const action = name.slice(0, -2) + "_A";
      if (this.hasAnimation(action)) {
        this.char.state.setAnimation(2, action, this.loopAnimation);
      }
    } else {
      this.char.state.clearTrack(2);
    }

    // If other than idle, play idle
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

  /**
   * Get an animation.
   * @param name - Animation name
   */
  getAnimation(name: string) {
    if (!this.char) return;

    const animations = this.char.state.data.skeletonData.animations;
    const animation = animations.find((a) => a.name === name);
    return animation;
  }

  /**
   * Get a list of animations.
   * @returns {string[]}
   */
  getAnimations(): string[] {
    if (!this.char) return [];

    const animations = this.char.state.data.skeletonData.animations;
    const names = animations.map((a) => a.name);
    return names;
  }

  get loopAnimation(): boolean {
    return this._loopAnimation;
  }

  set loopAnimation(v: boolean) {
    if (!this.char) return;

    if (this.howl !== undefined) this.howl.stop();

    this._loopAnimation = v;
    this.char.state.tracks[0]!.loop = v;
  }
}
