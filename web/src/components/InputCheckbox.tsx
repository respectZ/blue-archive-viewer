interface InputCheckboxProps {
  id: string;
  label: string;
  onChange: (value: boolean) => void;
  defaultChecked?: boolean;
  ref?: (el: HTMLInputElement) => void;
}

export function InputCheckbox(props: InputCheckboxProps) {
  return (
    <div class="flex items-center gap-3">
      <input
        type="checkbox"
        name={props.id}
        id={props.id}
        class="h-5 w-5 cursor-pointer rounded border-(--border) bg-(--bg-base) text-(--accent) accent-(--accent) focus:ring-2 focus:ring-(--accent)/30"
        checked={props.defaultChecked ?? false}
        onChange={(e) => {
          props.onChange((e.currentTarget as HTMLInputElement).checked);
        }}
        ref={props.ref}
      />
      <label
        for={props.id}
        class="cursor-pointer text-sm text-(--text-secondary)"
      >
        {props.label}
      </label>
    </div>
  );
}
