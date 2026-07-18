import { A } from "@solidjs/router";

export function NotFound() {
  return (
    <div class="flex min-h-full flex-col items-center justify-center px-6 py-20">
      <div class="relative mb-6">
        <div class="absolute -inset-6 rounded-full border border-[var(--accent)]/20 opacity-50" />
        <div class="absolute -inset-10 rounded-full border border-[var(--accent)]/10 opacity-30" />
        <h1 class="relative text-7xl font-bold text-[var(--accent)] drop-shadow-[0_0_24px_var(--accent-glow)]">
          404
        </h1>
      </div>
      <p class="mb-8 text-lg text-[var(--text-secondary)]">Page not found</p>
      <A
        href="/"
        class="rounded-lg border border-[var(--border-accent)] bg-[var(--surface-raised)] px-5 py-2.5 text-sm font-medium text-[var(--text-primary)] transition-all hover:border-[var(--accent)] hover:bg-[var(--accent)]/10 hover:shadow-[0_0_16px_var(--accent-glow)]"
      >
        Home
      </A>
    </div>
  );
}
