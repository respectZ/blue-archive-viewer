import { onMount, createSignal, createEffect, For, Show, onCleanup } from "solid-js";
import { Navbar } from "../components/Navbar";

interface MediaResource {
  FileName: string;
  Path: string;
}

interface MediaCatalog {
  Table: Record<string, MediaResource>;
}

function GalleryImage(props: { src: string; alt?: string; onClick?: () => void }) {
  return (
    <img
      src={props.src}
      alt={props.alt ?? "Image"}
      class="aspect-square w-full cursor-pointer rounded-xl border border-[var(--border)] bg-[var(--surface)] object-cover transition-all duration-300 hover:scale-[1.03] hover:border-[var(--border-accent)] hover:shadow-[0_0_24px_var(--accent-glow)]"
      loading="lazy"
      onClick={props.onClick}
    />
  );
}

export function JPGallery() {
  const [images, setImages] = createSignal<MediaResource[]>([]);
  const [loadedImages, setLoadedImages] = createSignal<MediaResource[]>([]);
  const [modalImage, setModalImage] = createSignal("");
  const [modalVisible, setModalVisible] = createSignal(false);
  let bottomRef: HTMLDivElement | undefined;

  onMount(async () => {
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
  });

  createEffect(() => {
    const allImages = images();
    const loaded = loadedImages();
    if (allImages.length === 0) return;
    if (loaded.length >= allImages.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const currentLoaded = loadedImages().length;
            const subset = allImages.slice(currentLoaded, currentLoaded + 20);
            if (subset.length > 0) {
              setLoadedImages((prev) => [...prev, ...subset]);
            }
            observer.unobserve(entry.target);
          }
        });
      },
      { root: null, rootMargin: "0px", threshold: 0.1 }
    );

    if (bottomRef) {
      observer.observe(bottomRef);
    }

    onCleanup(() => observer.disconnect());
  });

  function openModal(path: string) {
    setModalImage(path);
    setTimeout(() => setModalVisible(true), 50);
  }

  function closeModal() {
    setModalVisible(false);
    setTimeout(() => setModalImage(""), 300);
  }

  return (
    <main class="h-full w-full flex flex-col">
      <Navbar region="jp" />

      <Show when={loadedImages().length === 0}>
        <div class="fixed inset-0 z-50 flex items-center justify-center bg-[var(--bg-base)]/90 backdrop-blur">
          <div class="relative flex flex-col items-center gap-4">
            <div class="h-12 w-12 animate-spin rounded-full border-2 border-[var(--border)] border-t-[var(--accent)] shadow-[0_0_16px_var(--accent-glow)]" />
            <p class="text-lg font-medium text-[var(--text-secondary)]">Loading...</p>
          </div>
        </div>
      </Show>

      <div
        class="fixed inset-0 z-40 flex items-center justify-center bg-[var(--bg-base)]/90 p-4 backdrop-blur transition-all duration-300"
        classList={{
          "opacity-0 pointer-events-none": !modalVisible(),
          "opacity-100": modalVisible(),
        }}
        onClick={closeModal}
      >
        <Show when={modalImage() !== ""}>
          <img
            src={modalImage()}
            alt={modalImage()}
            class="max-h-[85vh] max-w-[90vw] rounded-xl object-contain shadow-[0_0_40px_var(--accent-glow)] transition-all duration-150 hover:scale-[1.02]"
          />
        </Show>
      </div>

      <div class="grid w-full grid-cols-2 gap-3 p-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6">
        <For each={loadedImages()}>
          {(image) => (
            <GalleryImage
              src={image.Path}
              alt={image.FileName}
              onClick={() => openModal(image.Path)}
            />
          )}
        </For>
      </div>

      <div
        ref={bottomRef!}
        class="w-full py-8 text-center text-sm text-[var(--text-muted)]"
      >
        {loadedImages().length < images().length ? "Loading more images..." : ""}
      </div>
    </main>
  );
}
