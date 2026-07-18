export const toast = (message: string) => {
  const container = document.createElement("div");
  container.className = "w-full h-auto fixed top-24 flex justify-center items-center";
  const content = document.createElement("div");
  content.className = "bg-rose-700 px-4 py-3 shadow-lg rounded-md transition-all duration-1000 opacity-100";
  const text = document.createElement("p");
  text.className = "text-gray-100 text-xl";
  text.innerText = message;
  content.appendChild(text);
  container.appendChild(content);
  document.body.appendChild(container);
  setTimeout(() => {
    content.style.opacity = "0";
    setTimeout(() => {
      document.body.removeChild(container);
    }, 1000);
  }, 3000);
};
