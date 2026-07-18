import { defineConfig } from "vite";
import solidPlugin from "vite-plugin-solid";
import tailwindcss from "@tailwindcss/vite";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig(({ command }) => ({
  plugins: [solidPlugin(), tailwindcss()],
  publicDir: command === "serve" ? "../public" : false,
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

