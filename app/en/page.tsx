import Box from "../component/box";
import Navbar from "../component/navbar";

export default function Home() {
  return (
    <main className="h-screen w-screen flex flex-col">
      <Navbar region="en" />

      <div className="flex lg:flex-row flex-col justify-center items-center grow">
        <div className="bg-neutral-800 bg-opacity-80 px-4 py-1.5 rounded-md">
          <p className="text-2xl">Work in progress...</p>
        </div>
      </div>
    </main>
  );
}
