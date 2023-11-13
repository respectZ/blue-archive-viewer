export const toast = (message: string) => {
  const toast = document.createElement("div");
  toast.className = "w-full h-auto fixed top-24 flex justify-center items-center";
  const toastContent = document.createElement("div");
  toastContent.className = "bg-rose-700 px-4 py-3 shadow-lg rounded-md transition-all duration-1000 opacity-100";
  const toastText = document.createElement("p");
  toastText.className = "text-gray-100 text-xl";
  toastText.id = "toast";
  toastText.innerText = message;
  toastContent.appendChild(toastText);
  toast.appendChild(toastContent);
  document.body.appendChild(toast);
  setTimeout(() => {
    toastContent.style.opacity = "0";
    setTimeout(() => {
      document.body.removeChild(toast);
    }, 1000);
  }, 3000);
};
