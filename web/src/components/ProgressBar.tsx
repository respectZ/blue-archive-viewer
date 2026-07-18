import { JSX } from "solid-js";

interface ProgressBarProps {
  percent?: number;
  height?: number;
  children?: JSX.Element;
  class?: string;
  ref?: (el: HTMLDivElement) => void;
}

export function ProgressBar(props: ProgressBarProps) {
  const percent = () => props.percent ?? 0;
  const height = () => props.height ?? 8;

  return (
    <div class={props.class}>
      <div
        class="w-full overflow-hidden rounded-full bg-(--border)"
        style={{ height: `${height()}px` }}
      >
        <div
          class="h-full rounded-full bg-(--accent) shadow-[0_0_12px_var(--accent-glow)] transition-all duration-200"
          style={{ width: `${percent()}%` }}
          ref={props.ref}
        />
      </div>
      {props.children}
    </div>
  );
}
