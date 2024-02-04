import { IAnimationStateListener, ITrackEntry } from "pixi-spine";
import * as l2d from "./live2d_viewer";

export class Live2DViewer extends l2d.Live2DViewer {
  private isIdle = false;
  private _scale = 1;
  private startListener: IAnimationStateListener = {
    end: () => {},
  };
  private talkListener: IAnimationStateListener = {
    end: () => {},
  };
  listener: IAnimationStateListener = {
    end: (entry) => {},
    start: (entry) => {},
  };
  private _currentAnimation: string = "";
  constructor(canvas: HTMLCanvasElement) {
    super(canvas);
    this.talkListener.complete = this.onTalkComplete.bind(this);
    this.startListener.complete = this.onStartComplete.bind(this);
  }

  private onStartComplete(entry: ITrackEntry) {
    if (!this.char) return;
    this.playAnimation("Idle_01");
    this.loopAnimation = true;
    this.isIdle = true;
    this.char.state.removeListener(this.startListener);
    this._currentAnimation = "";
  }

  private onTalkComplete(entry: ITrackEntry) {
    if (!this.char) return;
    if (entry.trackIndex !== 1 && entry.trackIndex !== 2) return;

    this.isIdle = true;
    this.char.state.clearTrack(1);
    this.char.state.clearTrack(2);
    this.char.state.removeListener(this.talkListener);
    this._currentAnimation = "";
  }

  /**
   * Run a function when the animation ends.
   * @param listener Function to run when the animation ends
   */
  setListener(listener: IAnimationStateListener) {
    this.listener = listener;
    this.char!.state.addListener(this.listener);
  }

  /**
   * Clear the end listener for the animation.
   */
  clearListener() {
    this.char!.state.removeListener(this.listener);
    this.listener = {
      end: (entry) => {},
      start: (entry) => {},
    };
  }

  start() {
    if (!this.char) return;
    if (this.getAnimation("Start_Idle_01") == null) return;

    this._currentAnimation = "Start_Idle_01";
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

  /**
   * Play random talk animation
   * @returns Animation name
   */
  randomTalk() {
    if (!this.char) return;
    if (this.howl !== undefined) this.howl.stop();
    if (!this.isIdle) return;

    const animations = this.getAnimations().filter((x) => x.startsWith("Talk_") && x.endsWith("_M"));
    if (animations.length === 0) return;
    const random = Math.floor(Math.random() * animations.length);
    const animation = animations[random];
    this._currentAnimation = animation;

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

    const bones: string[] = this.char!.state.data.skeletonData.bones.map((x) => x.name);
    console.log(bones);
    // this.char!.
  }
}
