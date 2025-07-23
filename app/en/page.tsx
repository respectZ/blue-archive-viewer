import Image from "next/image";
import Box from "../component/box";
import Navbar from "../component/navbar";

export default function Home() {
  return (
    <main className="h-screen w-screen flex flex-col">
      <Navbar region="en" />

      <div className="flex lg:flex-row flex-col justify-center items-center grow">
        <Box
          bg="data/jp/MediaResources/GameData/UIs/03_Scenario/01_Background/BG_CS_PV3_54.jpg"
          label="Live2D"
          href="/en/live2d"
        ></Box>
      </div>
    </main>
  );
}
