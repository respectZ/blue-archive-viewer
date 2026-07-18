import { JSX } from "solid-js";

interface ModalProps {
  children?: JSX.Element;
  class?: string;
  ref?: (el: HTMLDivElement) => void;
}

export function Modal(props: ModalProps) {
  return (
    <div
      class={`fixed inset-0 z-50 flex items-center justify-center bg-(--bg-base)/80 p-4 backdrop-blur-sm ${props.class ?? ""}`}
      ref={props.ref}
    >
      <div class="max-h-[90vh] w-full max-w-2xl overflow-auto rounded-2xl border border-(--border-accent) bg-(--surface) p-6 shadow-[0_0_40px_var(--accent-glow)]">
        {props.children}
      </div>
    </div>
  );
}
