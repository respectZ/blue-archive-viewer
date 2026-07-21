export const get_origin = () => {
  const base = import.meta.env.VITE_ASSET_BASE;
  if (base) return base;

  if (window.location.origin !== "file://") return window.location.origin;

  const scriptElement = document.createElement("script");
  scriptElement.src = "dummy.js";
  const scriptUrl = scriptElement.src;
  return scriptUrl.substring(0, scriptUrl.lastIndexOf("/") + 1);
};
