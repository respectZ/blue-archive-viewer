export const runOnClient = (func: () => any) => {
  if (typeof window !== "undefined") {
    if (window.document.readyState == "loading") {
      window.addEventListener("load", func);
    } else {
      func();
    }
  }
};
