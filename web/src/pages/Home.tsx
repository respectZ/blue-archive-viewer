import { A } from "@solidjs/router";

export function Home() {
  return (
    <div class="flex min-h-full flex-col items-center justify-center px-6 py-20">
      <div class="relative mb-10 text-center">
        <div class="absolute -inset-10 rounded-full border border-[var(--accent)]/10 opacity-60" />
        <div class="absolute -inset-16 rounded-full border border-[var(--accent)]/5 opacity-40" />
        <h1 class="relative text-5xl font-bold tracking-tight text-[var(--text-primary)] sm:text-6xl">
          Blue Archive
        </h1>
        <p class="relative mt-3 text-lg text-[var(--text-secondary)]">Resource Viewer</p>
      </div>

      <nav class="relative z-10 grid w-full max-w-4xl grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <A
          href="/jp"
          class="group relative overflow-hidden rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-6 text-center shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-[var(--border-accent)] hover:shadow-[0_0_28px_var(--accent-glow)]"
        >
          <span class="relative z-10 text-xl font-semibold text-[var(--text-primary)] transition-colors group-hover:text-[var(--accent)]">
            JP
          </span>
          <div class="absolute inset-0 bg-gradient-to-br from-[var(--accent)]/5 to-transparent opacity-0 transition-opacity group-hover:opacity-100" />
        </A>
        <A
          href="/en"
          class="group relative overflow-hidden rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-6 text-center shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-[var(--border-accent)] hover:shadow-[0_0_28px_var(--accent-glow)]"
        >
          <span class="relative z-10 text-xl font-semibold text-[var(--text-primary)] transition-colors group-hover:text-[var(--accent)]">
            EN
          </span>
          <div class="absolute inset-0 bg-gradient-to-br from-[var(--accent)]/5 to-transparent opacity-0 transition-opacity group-hover:opacity-100" />
        </A>
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
          href="/wpengine"
          class="group relative overflow-hidden rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-6 text-center shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-[var(--border-accent)] hover:shadow-[0_0_28px_var(--accent-glow)]"
        >
          <span class="relative z-10 text-xl font-semibold text-[var(--text-primary)] transition-colors group-hover:text-[var(--accent)]">
            Wallpaper Engine
          </span>
          <div class="absolute inset-0 bg-gradient-to-br from-[var(--accent)]/5 to-transparent opacity-0 transition-opacity group-hover:opacity-100" />
        </A>
      </nav>
    </div>
  );
}
