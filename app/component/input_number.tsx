export default function InputNumber(
  props: {
    id: string;
    label: string;
    onChange?: (value: number) => void;
    reference?: React.MutableRefObject<HTMLInputElement | null>;
    step?: number;
    max?: number;
    min?: number;
    defaultValue?: number;
  },
) {
  return (
    <div className="flex flex-col">
      <div className="flex flex-row items-center justify-center">
        <label htmlFor={props.id} className="text-l mr-2 text-gray-200">
          {props.label}
        </label>
        <input
          type="number"
          className="h-10 text-gray-100 rounded-l bg-neutral-950 border-gray-400 border-2 flex-grow"
          name={props.id}
          id={props.id}
          onChange={(e) => {
            // Call onChange
            if (props.onChange) props.onChange(e.target.valueAsNumber);
          }}
          defaultValue={props.defaultValue ? props.defaultValue : props.min ? props.min : 0}
          step={props.step ? props.step : 1}
          max={props.max ? props.max : 100}
          min={props.min ? props.min : 0}
          ref={props.reference}
        />
      </div>
    </div>
  );
}
