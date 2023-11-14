interface ProgressBarProps {
  percent?: number;
  height?: number;
  children?: React.ReactNode;
  className?: string;
  reference?: React.MutableRefObject<HTMLDivElement | null>;
}

const ProgressBar: React.FC<ProgressBarProps> = ({ percent = 0, children, className, height = 8, reference }) => {
  return (
    <div className={className}>
      <div className={`bg-gray-200 w-full h-${height} rounded-md`}>
        <div className={`bg-rose-700 h-${height} rounded-md duration-200 transition-all`} style={{ width: `${percent}%` }} ref={reference}></div>
      </div>
      {children}
    </div>
  );
};

export default ProgressBar;
