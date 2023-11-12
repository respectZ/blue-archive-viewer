"use client";

interface BoxProps {
  bg?: string;
  href?: string;
  label?: string;
  opacity?: number;
  children: React.ReactNode;
}

const Box: React.FC<BoxProps> = ({ bg, href, label, opacity, children }) => {
  return (
    <div
      className="duration-300 transition-all h-48 w-48 sm:h-24 sm:w-24 md:h-24 md:w-24 xl:h-96 xl:w-96 shadow-xl rounded-xl m-4 hover:shadow-2xl hover:scale-110 cursor-pointer"
      onClick={() => window.open(href ?? "#", "_self")}
    >
      <div
        className="rounded-xl h-full w-full bg-center bg-cover"
        style={{ backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, ${opacity ?? 0.6}), rgba(0, 0, 0, ${opacity ?? 0.6})), url(${bg ?? ""})` }}
      >
        <div className="h-full w-full flex flex-col items-center justify-center">
          <p className="text-4xl text-gray-100">{label ?? ""}</p>
        </div>
      </div>
    </div>
  );
};

export default Box;
