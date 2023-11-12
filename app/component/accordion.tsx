// components/Accordion.tsx
import React, { ReactNode, useState } from "react";

interface AccordionProps {
  title: string;
  children: ReactNode;
}

const Accordion: React.FC<AccordionProps> = ({ title, children }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleAccordion = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="mb-4">
      <div className="cursor-pointer flex justify-between items-center" onClick={toggleAccordion}>
        <span className="text-4xl text-gray-200">{title}</span>
        <svg
          className={`w-4 h-4 transform transition-transform duration-300 ${isOpen ? "rotate-180" : "rotate-0"}`}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          fill="#fff"
        >
          <path d="M7 10l5 5 5-5z" />
        </svg>
      </div>
      <div
        className={`transition-max-height duration-300 ease-in-out overflow-hidden ${isOpen ? "max-h-screen" : "max-h-0"}`}
      >
        <div className="p-2 mt-4">{children}</div>
      </div>
    </div>
  );
};

export default Accordion;
