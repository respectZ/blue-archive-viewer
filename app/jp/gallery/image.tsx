"use client";

import Image from "next/image";

export default function ImageComponent(
  props: {
    src: string;
    alt?: string;
    height?: number;
    width?: number;
    onClick?: () => void;
  },
) {
  return (
    <Image
      src={props.src}
      alt={props.alt ?? "Image"}
      height={props.height ?? 300}
      width={props.width ?? 300}
      className="transition-all duration-300 hover:scale-110 shadow-md hover:shadow-2xl border-gray-100 border-4 m-4 cursor-pointer"
      loading="lazy"
      onClick={props.onClick}
    >
    </Image>
  );
}
