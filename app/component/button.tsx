export default function Button(
  props: {
    id: string;
    label: string;
    onClick?: () => void;
    reference?: React.MutableRefObject<HTMLButtonElement | null>;
  },
) {
  return (
    <button
      id={props.id}
      className="px-4 py-1.5 mb-2 mr-2 transition-all duration-300 text-gray-100 hover:text-neutral-950 bg-transparent hover:bg-gray-200 hover:scale-110 border-gray-400 hover:border-neutral-500 border-2 rounded-md"
      onClick={props.onClick}
      ref={props.reference}
    >
      <span className="text-xl">{props.label}</span>
    </button>
  );
}
