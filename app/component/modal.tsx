"use client";

interface Modal extends React.HTMLAttributes<HTMLDivElement> {
  children?: React.ReactNode;
  className?: string;
  reference?: React.MutableRefObject<HTMLDivElement | null>;
}

const Modal: React.FC<Modal> = ({ children, className, reference, ...props }) => {
  return (
    <div className={`w-full h-full fixed flex justify-center items-center bg-black bg-opacity-70 z-50 ${className}`} {...props} ref={reference}>
      <div className={"bg-neutral-700 text-gray-200 h-auto w-auto p-8 shadow-xl rounded-md"}>
        {children}
      </div>
    </div>
  );
};

export default Modal;
