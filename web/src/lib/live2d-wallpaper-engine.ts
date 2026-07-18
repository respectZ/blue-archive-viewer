import { AnimationStateListener, Spine } from "@esotericsoftware/spine-pixi";
import {
  IAnimationStateListener,
  ITrackEntry,
  Spine as PixiSpine,
} from "pixi-spine";
import { Live2DEngine } from "./live2d-engine";

export class Live2DWallpaperEngine extends Live2DEngine {
  private isIdle = false;
  private _scale = 1;
  private startListener: IAnimationStateListener = {
    end: () => {},
  };
  private wallpaperTalkListener: IAnimationStateListener = {
    end: () => {},
  };
  listener: IAnimationStateListener = {
    end: (entry) => {},
    start: (entry) => {},
  };
  private _currentAnimation = "";

  constructor(canvas: HTMLCanvasElement) {
    super(canvas);
    this.wallpaperTalkListener.complete = this.onTalkComplete.bind(this);
    this.startListener.complete = this.onStartComplete.bind(this);
  }

  private onStartComplete(entry: ITrackEntry) {
    if (!this.char) return;
    this.playAnimation("Idle_01");
    this.loopAnimationValue = true;
    this.isIdle = true;
    if (this.char instanceof PixiSpine)
      this.char.state.removeListener(this.startListener);
    if (this.char instanceof Spine)
      this.char.state.removeListener(
        this.startListener as AnimationStateListener
      );
    this._currentAnimation = "";
  }

  private onTalkComplete(entry: ITrackEntry) {
    if (!this.char) return;
    if (entry.trackIndex !== 1 && entry.trackIndex !== 2) return;

    this.isIdle = true;
    this.char.state.setEmptyAnimation(1, 0.2);
    this.char.state.setEmptyAnimation(2, 0.2);
    if (this.char instanceof PixiSpine)
      this.char.state.removeListener(this.wallpaperTalkListener);
    if (this.char instanceof Spine)
      this.char.state.removeListener(
        this.wallpaperTalkListener as AnimationStateListener
      );
    this._currentAnimation = "";
  }

  setListener(listener: IAnimationStateListener) {
    this.listener = listener;
    if (this.char instanceof PixiSpine)
      this.char.state.addListener(this.listener);
    if (this.char instanceof Spine)
      this.char.state.addListener(this.listener as AnimationStateListener);
  }

  clearListener() {
    if (this.char instanceof PixiSpine)
      this.char.state.removeListener(this.listener);
    if (this.char instanceof Spine)
      this.char.state.removeListener(
        this.listener as AnimationStateListener
      );
    this.listener = {
      end: (entry: ITrackEntry) => {},
      start: (entry: ITrackEntry) => {},
    };
  }

  start() {
    if (!this.char) return;
    if (this.hasAnimation("Start_Idle_01") == null) return;

    this._currentAnimation = "Start_Idle_01";
    this.playAnimation("Start_Idle_01");

    if (this.char instanceof PixiSpine)
      this.char.state.addListener(this.startListener);
    if (this.char instanceof Spine)
      this.char.state.addListener(this.startListener as AnimationStateListener);
  }

  idle() {
    if (!this.char) return;
    if (this.hasAnimation("Idle_01") == null) return;

    this.playAnimation("Idle_01");
    this.loopAnimation = true;
    this.isIdle = true;
  }

  randomTalk() {
    if (!this.char) return;
    if (!this.isIdle) return;

    const animations = this.getAnimations().filter(
      (x) => x.startsWith("Talk_") && x.endsWith("_M")
    );
    if (animations.length === 0) return;
    const random = Math.floor(Math.random() * animations.length);
    const animation = animations[random];
    this._currentAnimation = animation;

    if (animation.endsWith("_M")) {
      const action = animation.slice(0, -2) + "_A";
      if (this.hasAnimation(action)) {
        this.char.state.setAnimation(2, action, false);
      }
    } else {
      this.char.state.clearTrack(2);
    }

    this.isIdle = false;
    this.char.state.setAnimation(1, animation, false);
    if (this.char instanceof PixiSpine)
      this.char.state.addListener(this.wallpaperTalkListener);
    if (this.char instanceof Spine)
      this.char.state.addListener(this.wallpaperTalkListener as AnimationStateListener);

    return animation;
  }

  get currentAnimation() {
    return this._currentAnimation;
  }

  override scale(scale?: number) {
    this._scale = scale ?? this._scale;
    super.scale(scale);
  }

  override async loadModel(src: string) {
    await super.loadModel(src);
    this.scale(this._scale);

    if (this.char instanceof Spine) {
      this.char.state.data.defaultMix = 0.2;
    } else if (this.char instanceof PixiSpine) {
      this.char.stateData.defaultMix = 0.2;
    }
  }
}