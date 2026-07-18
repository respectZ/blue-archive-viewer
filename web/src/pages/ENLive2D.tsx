import { A } from "@solidjs/router";

export function ENLive2D() {
  return (
    <div class="flex min-h-full flex-col items-center justify-center px-6 py-20">
      <div class="relative w-full max-w-md rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-8 shadow-lg">
        <div class="absolute -inset-px rounded-2xl border border-[var(--accent)]/10" />
        <h1 class="relative text-2xl font-bold text-[var(--text-primary)]">EN Live2D</h1>
        <p class="relative mt-2 text-[var(--text-secondary)]">
          Phase 0 scaffold — live2d viewer port lands in Phase 3.
        </p>
        <A
          href="/en"
          class="relative mt-6 inline-block text-sm font-medium text-[var(--text-muted)] transition-colors hover:text-[var(--accent)]"
        >
          Back
        </A>
      </div>
    </div>
  );
}
