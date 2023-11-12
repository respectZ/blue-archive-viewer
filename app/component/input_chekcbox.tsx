export default function InputCheckbox(
  props: {
    id: string;
    label: string;
    onChange: (value: boolean) => void;
    defaultChecked?: boolean;
    reference?: React.MutableRefObject<HTMLInputElement | null>;
  },
) {
  return (
    <div className="flex flex-col">
      <div className="flex flex-row">
        <input
          type="checkbox"
          name={props.id}
          id={props.id}
          className="mr-2"
          defaultChecked={props.defaultChecked ? props.defaultChecked : false}
          onChange={(e) => {
            // Call onChange
            props.onChange(e.target.checked);
          }}
          ref={props.reference}
        />
        <label htmlFor={props.id} className="text-l">{props.label}</label>
      </div>
    </div>
  );
}
