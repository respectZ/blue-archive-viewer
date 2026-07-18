interface NavbarProps {
  region?: string;
}

export function Navbar(props: NavbarProps) {
  return (
    <header class="sticky top-0 z-40 flex h-14 w-full items-center border-b border-(--border) bg-(--surface)/80 px-6 backdrop-blur-md">
      <button
        class="group relative flex items-center gap-3 text-(--accent) transition-colors hover:text-(--accent-soft)"
        onClick={() => {
          const baseUrl = window.location.href.split("/")[0];
          window.location.href = baseUrl + "/" + (props.region ?? "jp");
        }}
      >
        <span class="absolute -inset-3 rounded-full border border-(--accent)/10 opacity-0 transition-all duration-500 group-hover:scale-110 group-hover:opacity-100" />
        <span class="absolute -inset-3 rounded-full border border-(--accent)/5 opacity-0 transition-all duration-700 group-hover:scale-125 group-hover:opacity-100" />
        <span class="relative h-2.5 w-2.5 rounded-full bg-(--accent) shadow-[0_0_12px_var(--accent)]" />
        <span class="relative text-lg font-bold tracking-wide">
          Blue Archive
        </span>
      </button>
    </header>
  );
}
