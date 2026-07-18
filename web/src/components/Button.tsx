interface ButtonProps {
  id: string;
  label: string;
  onClick?: () => void;
  ref?: (el: HTMLButtonElement) => void;
}

export function Button(props: ButtonProps) {
  return (
    <button
      id={props.id}
      class="inline-flex items-center justify-center rounded-lg border border-(--border-accent) bg-(--surface-raised) px-4 py-2 text-sm font-medium text-(--text-primary) shadow-sm transition-all duration-200 hover:border-(--accent) hover:bg-(--accent)/10 hover:shadow-[0_0_16px_var(--accent-glow)] active:scale-95"
      onClick={props.onClick}
      ref={props.ref}
    >
      {props.label}
    </button>
  );
}
