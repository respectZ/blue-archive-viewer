import { createSignal, For } from "solid-js";

interface InputSelectProps {
  id: string;
  label: string;
  options: { value: string; label: string }[];
  value?: string;
  onChange: (value: string) => void;
  ref?: (el: HTMLSelectElement) => void;
}

export function InputSelect(props: InputSelectProps) {
  const [selected, setSelected] = createSignal(props.value ?? "");

  const handleChange = (e: Event) => {
    const val = (e.currentTarget as HTMLSelectElement).value;
    setSelected(val);
    props.onChange(val);
  };

  return (
    <div class="flex flex-col gap-1">
      <label for={props.id} class="text-sm font-medium text-(--text-secondary)">
        {props.label}
      </label>
      <div class="relative">
        <select
          ref={props.ref}
          id={props.id}
          class="h-10 w-full appearance-none rounded-lg border border-(--border) bg-(--bg-base) px-3 pr-8 text-sm text-(--text-primary) transition focus:border-(--accent) focus:outline-none focus:ring-2 focus:ring-(--accent)/30"
          onChange={handleChange}
        >
          <For each={props.options}>
            {(option) => (
              <option
                value={option.value}
                selected={option.value === selected()}
              >
                {option.label}
              </option>
            )}
          </For>
        </select>
        <svg
          class="pointer-events-none absolute right-2.5 top-1/2 h-4 w-4 -translate-y-1/2 text-(--text-muted)"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path d="M7 10l5 5 5-5z" />
        </svg>
      </div>
    </div>
  );
}
