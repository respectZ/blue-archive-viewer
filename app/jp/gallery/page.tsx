"use client";

import ImageComponent from "./image";
import Navbar from "../../component/navbar";
import { useEffect, useRef, useState } from "react";
import Image from "next/image";

interface MediaResource {
  FileName: string;
  Path: string;
}

interface MediaCatalog {
  Table: Record<string, MediaResource>;
}

export default function Home() {
  const [images, setImages] = useState<MediaResource[]>([]);
  const [loadedImages, setLoadedImages] = useState<MediaResource[]>([]);
  const bottomRef = useRef<HTMLDivElement>(null);
  const [modalImage, setModalImage] = useState<string>("");
  const modalRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (images.length > 0) return;
    const fetchData = async () => {
      const response = await fetch("/data/jp/MediaResources/MediaCatalog.json");
      const data: MediaCatalog = await response.json();
      setImages(
        Object.keys(data.Table)
          .map((key) => {
            const v = data.Table[key];
            if (!v.Path.endsWith(".jpg")) return null;
            v.Path = `/data/jp/MediaResources/${v.Path}`;
            return v;
          })
          .filter((v) => v !== null) as MediaResource[]
      );
    };
    fetchData();
  }, [images]);

  useEffect(() => {
    const loadMore = () => {
      const subset = images.slice(
        loadedImages.length,
        loadedImages.length + 20
      );
      setLoadedImages((prev) => [...prev, ...subset]);
    };

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            loadMore();
            observer.unobserve(entry.target);
          }
        });
      },
      { root: null, rootMargin: "0px", threshold: 0.1 }
    );

    if (bottomRef.current) {
      observer.observe(bottomRef.current);
    }
  }, [images, loadedImages]);

  return (
    <main className="h-full w-full flex flex-col">
      <Navbar region="jp" />

      {loadedImages.length > 0 ? null : (
        <div className="fixed h-full w-full">
          <div className="absolute h-full w-full bg-black bg-opacity-60 flex items-center justify-center">
            <div className="text-white text-4xl">Loading...</div>
          </div>
        </div>
      )}

      <div
        className={
          "fixed h-full w-full z-10 transition-all duration-300 opacity-0 hidden"
        }
        ref={modalRef}
      >
        <div
          className={
            "absolute h-full w-full bg-black bg-opacity-60 flex items-center justify-center"
          }
          onClick={() => {
            if (modalRef.current) {
              setTimeout(() => {
                setModalImage("");
                modalRef.current!.classList.add("hidden");
              }, 300);
              modalRef.current.classList.add("opacity-0");
              modalRef.current.classList.remove("opacity-100");
            }
          }}
        >
          <Image
            src={modalImage}
            alt={modalImage}
            fill
            style={{ objectFit: "contain" }}
            className="p-24 flex items-end transition-all duration-150 hover:scale-105 ease-out"
          />
        </div>
      </div>

      <div className="flex flex-wrap justify-center items-center">
        {loadedImages.map((image, i) => {
          return (
            <ImageComponent
              key={i}
              src={image.Path}
              alt={image.FileName}
              onClick={() => {
                setModalImage(image.Path);
                if (modalRef.current) {
                  setTimeout(() => {
                    modalRef.current!.classList.add("opacity-100");
                    modalRef.current!.classList.remove("opacity-0");
                  }, 1);
                  modalRef.current!.classList.remove("hidden");
                }
              }}
            />
          );
        })}
        <div ref={bottomRef}>
          {loadedImages.length < images.length ? "Loading more images..." : ""}
        </div>
      </div>
    </main>
  );
}
