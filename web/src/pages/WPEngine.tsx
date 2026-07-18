import { A } from "@solidjs/router";

export function WPEngine() {
  return (
    <div class="flex min-h-full flex-col items-center justify-center px-6 py-20">
      <div class="relative w-full max-w-md rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-8 shadow-lg">
        <div class="absolute -inset-px rounded-2xl border border-[var(--accent)]/10" />
        <h1 class="relative text-2xl font-bold text-[var(--text-primary)]">Wallpaper Engine</h1>
        <p class="relative mt-2 text-[var(--text-secondary)]">
          Phase 0 scaffold — WPEngine port lands in Phase 5.
        </p>
        <A
          href="/"
          class="relative mt-6 inline-block text-sm font-medium text-[var(--text-muted)] transition-colors hover:text-[var(--accent)]"
        >
          Back
        </A>
      </div>
    </div>
  );
}
