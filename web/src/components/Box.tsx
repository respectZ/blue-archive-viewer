interface BoxProps {
  bg?: string;
  href?: string;
  label?: string;
  opacity?: number;
}

export function Box(props: BoxProps) {
  return (
    <div
      class="group relative cursor-pointer overflow-hidden rounded-2xl border border-(--border) bg-(--surface) shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-(--border-accent) hover:shadow-[0_0_28px_var(--accent-glow)]"
      onClick={() => window.open(props.href ?? "#", "_self")}
    >
      <div
        class="h-full w-full bg-center bg-cover"
        style={{
          "background-image": `linear-gradient(to top, rgba(3, 7, 17, ${props.opacity ?? 0.75}), rgba(3, 7, 17, ${(props.opacity ?? 0.75) * 0.4})), url(${props.bg ?? ""})`,
        }}
      >
        <div class="flex h-full w-full flex-col items-center justify-center p-6">
          <span class="text-center text-xl font-semibold text-(--text-primary) transition-colors group-hover:text-(--accent)">
            {props.label ?? ""}
          </span>
        </div>
      </div>
    </div>
  );
}
