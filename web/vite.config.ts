import { defineConfig } from "vite";
import solidPlugin from "vite-plugin-solid";
import tailwindcss from "@tailwindcss/vite";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig(() => ({
  plugins: [solidPlugin(), tailwindcss()],
  publicDir: "../public",
  resolve: {
    alias: {
      "~": path.resolve(__dirname, "src"),
    },
  },
  css: {
    postcss: {},
  },
  build: {
    outDir: "dist",
    target: "esnext",
    chunkSizeWarningLimit: 1000,
  },
  server: {
    port: 3000,
  },
}));

