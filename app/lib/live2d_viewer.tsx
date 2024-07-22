import "pixi-spine";

import * as PIXI from "pixi.js";
import { Spine } from "pixi-spine";
import { Howl, Howler } from "howler";
import { AddressablesCatalogUrlRoot } from "../jp/url";

function calculateFitScale(
  srcWidth: number,
  srcHeight: number,
  maxWidth: number,
  maxHeight: number,
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
  maxHeight: number,
) {
  const widthScale = maxWidth / srcWidth;
  const heightScale = maxHeight / srcHeight;

  console.log(`widthScale: ${widthScale} heightScale: ${heightScale}`);

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
  char?: Spine;

  playVoice: boolean = false;
  voiceVolume: number = 1;
  howl?: Howl;
  baseURL: string = AddressablesCatalogUrlRoot;
  private _loopAnimation: boolean = false;

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

    // Play default animation
    // Ignore case
    const startAnimation = this.getAnimations().find((a) => a.toLowerCase() === "start_idle_01");
    if (startAnimation) {
      this.playAnimation(startAnimation);
    } else {
      const animation = char.state.data.skeletonData.animations[0];
      this.playAnimation(animation.name);
    }

    char.state.addListener(
      {
        event: async (entry, event) => {
          if (!this.playVoice) return;
          if (event.data.name !== "Talk") return;

          if (this.howl !== undefined) this.howl.stop();

          const data = event as any as EventData;

          let fileName = data.stringValue + ".ogg";
          let characterId = fileName.split("_")[0];

          let src = `${this.baseURL}/MediaResources/Audio/VOC_JP/JP_${characterId}/${fileName}`;

          // Try to fetch first, if not found, try title case characterId (error case: hinata_home, should be Hinata in fileName)
          // Also disable cors
          const res = await fetch(src, { mode: "no-cors" });
          if (!res.ok) {
            characterId = characterId[0].toUpperCase() + characterId.slice(1);
            fileName = fileName[0].toUpperCase() + fileName.slice(1);
            src = `${this.baseURL}/MediaResources/Audio/VOC_JP/JP_${characterId}/${fileName}`;
          }

          this.howl = new Howl({
            volume: this.voiceVolume,
            src: `${this.baseURL}/MediaResources/Audio/VOC_JP/JP_${characterId}/${fileName}`,
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
      },
    );
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
   * @returns {Promise<Spine>}
   * @example
   * const live2d = new Live2DViewer(...);
   * live2d.addSpine("data/akari_home/akari_bg.skel", "bg", 0);
   */
  async addSpine(src: string, name: string, index?: number): Promise<Spine> {
    const data = await PIXI.Assets.load(src);
    const spine = new Spine(data.spineData);
    spine.name = name;

    if (index !== undefined) {
      this.app.stage.addChildAt(spine, index);
    } else {
      this.app.stage.addChild(spine);
    }

    let scale = calculateFillScale(
      spine.spineData.width,
      spine.spineData.height,
      this.app.renderer.width,
      this.app.renderer.height,
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
      if (!(child instanceof Spine)) return;

      let scaleX = width ? (width / child.spineData.width) : (child.scale.x);
      let scaleY = height ? (height / child.spineData.height) : (child.scale.y);

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
      if (!(child instanceof Spine)) return;
      let scale = calculateFillScale(
        child.spineData.width,
        child.spineData.height,
        this.app.renderer.width,
        this.app.renderer.height,
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
      if (!(child instanceof Spine)) return;
      let scale = calculateFitScale(
        child.spineData.width,
        child.spineData.height,
        this.app.renderer.width,
        this.app.renderer.height,
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
      if (!(child instanceof Spine)) return;

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
      if (!(child instanceof Spine)) return;
      child.x = this.app.renderer.width / 2;
      if (child.spineData.height * child.scale.y < this.app.renderer.height) {
        child.y = this.app.renderer.height -
          child.spineData.height * child.scale.y * 1.25;
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
      if (this.char.state.hasAnimation(action)) {
        this.char.state.setAnimation(2, action, this.loopAnimation);
      }
    } else {
      this.char.state.clearTrack(2);
    }

    // If other than idle, play idle
    if (!name.includes("Idle")) {
      if (this.char.state.hasAnimation("Idle_01")) {
        this.char.state.setAnimation(1, "Idle_01", true);
      }
    } else {
      this.char.state.clearTrack(1);
    }

    this.char.state.setAnimation(0, name, this.loopAnimation);
    this.char.state.addListener({ complete: options.onComplete });
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
    this.char.state.tracks[0].loop = v;
  }
}
