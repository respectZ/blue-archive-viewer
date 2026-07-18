import { A } from "@solidjs/router";

export function JP() {
  return (
    <div class="flex min-h-full flex-col items-center justify-center px-6 py-20">
      <div class="relative mb-8 text-center">
        <div class="absolute -inset-8 rounded-full border border-[var(--accent)]/10 opacity-60" />
        <h1 class="relative text-4xl font-bold tracking-tight text-[var(--text-primary)] sm:text-5xl">
          JP
        </h1>
      </div>

      <nav class="grid w-full max-w-md grid-cols-1 gap-4 sm:grid-cols-2">
        <A
          href="/jp/gallery"
          class="group relative overflow-hidden rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-6 text-center shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-[var(--border-accent)] hover:shadow-[0_0_28px_var(--accent-glow)]"
        >
          <span class="relative z-10 text-xl font-semibold text-[var(--text-primary)] transition-colors group-hover:text-[var(--accent)]">
            Gallery
          </span>
          <div class="absolute inset-0 bg-gradient-to-br from-[var(--accent)]/5 to-transparent opacity-0 transition-opacity group-hover:opacity-100" />
        </A>
        <A
          href="/jp/live2d"
          class="group relative overflow-hidden rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-6 text-center shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-[var(--border-accent)] hover:shadow-[0_0_28px_var(--accent-glow)]"
        >
          <span class="relative z-10 text-xl font-semibold text-[var(--text-primary)] transition-colors group-hover:text-[var(--accent)]">
            Live2D
          </span>
          <div class="absolute inset-0 bg-gradient-to-br from-[var(--accent)]/5 to-transparent opacity-0 transition-opacity group-hover:opacity-100" />
        </A>
      </nav>

      <A
        href="/"
        class="mt-10 text-sm font-medium text-[var(--text-muted)] transition-colors hover:text-[var(--accent)]"
      >
        Back
      </A>
    </div>
  );
}
