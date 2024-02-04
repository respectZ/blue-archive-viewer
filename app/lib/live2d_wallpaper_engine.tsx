import { IAnimationStateListener, ITrackEntry } from "pixi-spine";
import * as l2d from "./live2d_viewer";

export class Live2DViewer extends l2d.Live2DViewer {
  private isIdle = false;
  private startListener: IAnimationStateListener = {
    end: () => {},
  };
  private talkListener: IAnimationStateListener = {
    end: () => {},
  };
  constructor(canvas: HTMLCanvasElement) {
    super(canvas);
    this.talkListener.complete = this.onTalkComplete.bind(this);
    this.startListener.complete = this.onStartComplete.bind(this);
  }
  private _scale = 1;

  start() {
    if (!this.char) return;
    if (this.getAnimation("Start_Idle_01") == null) return;

    this.playAnimation("Start_Idle_01");

    this.char.state.addListener(this.startListener);
  }

  idle() {
    if (!this.char) return;
    if (this.getAnimation("Idle_01") == null) return;

    this.playAnimation("Idle_01");
    this.loopAnimation = true;
    this.isIdle = true;
  }

  private onStartComplete(entry: ITrackEntry) {
    if (!this.char) return;
    this.playAnimation("Idle_01");
    this.loopAnimation = true;
    this.isIdle = true;
    this.char.state.removeListener(this.startListener);
  }

  private onTalkComplete(entry: ITrackEntry) {
    if (!this.char) return;
    if (entry.trackIndex !== 1 && entry.trackIndex !== 2) return;

    this.isIdle = true;
    this.char.state.clearTrack(1);
    this.char.state.clearTrack(2);
    this.char.state.removeListener(this.talkListener);
  }

  randomTalk() {
    if (!this.char) return;
    if (this.howl !== undefined) this.howl.stop();
    if (!this.isIdle) return;

    const animations = this.getAnimations().filter((x) => x.startsWith("Talk_") && x.endsWith("_M"));
    if (animations.length === 0) return;
    const random = Math.floor(Math.random() * animations.length);
    const animation = animations[random];

    // If last animation name is M, play M (mouth/music?) + A (action?)
    if (animation.endsWith("_M")) {
      const action = animation.slice(0, -2) + "_A";
      if (this.char.state.hasAnimation(action)) {
        this.char.state.setAnimation(2, action, false);
      }
    } else {
      this.char.state.clearTrack(2);
    }

    this.isIdle = false;
    this.char.state.setAnimation(1, animation, false);
    this.char.state.addListener(this.talkListener);
  }

  override scale(scale?: number) {
    this._scale = scale ?? this._scale;
    super.scale(scale);
  }

  override async loadModel(src: string) {
    await super.loadModel(src);
    this.scale(this._scale);
  }
}
