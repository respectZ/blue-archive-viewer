interface InputNumberProps {
  id: string;
  label: string;
  onChange?: (value: number) => void;
  ref?: (el: HTMLInputElement) => void;
  step?: number;
  max?: number;
  min?: number;
  defaultValue?: number;
}

export function InputNumber(props: InputNumberProps) {
  return (
    <div class="flex flex-col gap-1">
      <label for={props.id} class="text-sm font-medium text-(--text-secondary)">
        {props.label}
      </label>
      <input
        type="number"
        class="h-10 w-full rounded-lg border border-(--border) bg-(--bg-base) px-3 text-sm text-(--text-primary) transition focus:border-(--accent) focus:outline-none focus:ring-2 focus:ring-(--accent)/30"
        name={props.id}
        id={props.id}
        onChange={(e) => {
          if (props.onChange)
            props.onChange((e.currentTarget as HTMLInputElement).valueAsNumber);
        }}
        value={props.defaultValue ?? props.min ?? 0}
        step={props.step ?? 1}
        max={props.max ?? 100}
        min={props.min ?? 0}
        ref={props.ref}
      />
    </div>
  );
}
