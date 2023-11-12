"use client";

export default function Navbar(
  props: {
    region?: string;
  },
) {
  return (
    <div className="flex flex-col bg-neutral-900 h-14 p-4 w-full justify-center z-0">
      <p
        className="text-2xl text-gray-100 cursor-pointer"
        onClick={() => {
          const baseUrl = window.location.href.split("/")[0];
          window.location.href = baseUrl + "/" + (props.region ?? "jp");
        }}
      >
        Blue Archive
      </p>
    </div>
  );
}
