export default function InputSelect(
  props: {
    id: string;
    label: string;
    options: { value: string; label: string }[];
    onChange: (value: string) => void;
    reference?: React.RefObject<HTMLSelectElement>;
  },
) {
  return (
    <div className="flex flex-col">
      <label htmlFor={props.id} className="text-xl mt-4 mb-2 text-gray-200">
        {props.label}
      </label>
      <select
        ref={props.reference}
        id={props.id}
        className="h-10 text-gray-100 rounded-l bg-neutral-950 border-gray-400 border-2"
        onChange={(e) => props.onChange(e.target.value)}
      >
        {props.options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}
