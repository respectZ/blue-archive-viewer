import { createSignal, JSX } from "solid-js";

interface AccordionProps {
  title: string;
  children: JSX.Element;
}

export function Accordion(props: AccordionProps) {
  const [isOpen, setIsOpen] = createSignal(false);

  const toggleAccordion = () => {
    setIsOpen(!isOpen());
  };

  return (
    <div class="border-b border-(--border) pb-4">
      <button
        class="flex w-full cursor-pointer items-center justify-between py-2 text-left"
        onClick={toggleAccordion}
      >
        <span class="text-lg font-semibold text-(--text-primary)">
          {props.title}
        </span>
        <svg
          class={`h-4 w-4 transform text-(--accent) transition-transform duration-300 ${isOpen() ? "rotate-180" : "rotate-0"}`}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path d="M7 10l5 5 5-5z" />
        </svg>
      </button>
      <div
        class={`overflow-hidden transition-all duration-300 ease-in-out ${isOpen() ? "max-h-screen opacity-100" : "max-h-0 opacity-0"}`}
      >
        <div class="pt-3">{props.children}</div>
      </div>
    </div>
  );
}
