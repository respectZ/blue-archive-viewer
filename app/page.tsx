import Image from "next/image";
import Box from "./component/box";
import Navbar from "./component/navbar";

export default function Home() {
  return (
    <main className="h-screen w-screen flex flex-col">
      <Navbar region="jp" />

      <div className="flex lg:flex-row flex-col justify-center items-center grow">
        <Box
          bg="data/jp/MediaResources/UIs/03_Scenario/01_Background/BG_CS_Arius_09.jpg"
          label="EN"
          href="/en/"
        >
        </Box>
        <Box
          bg="data/jp/MediaResources/UIs/03_Scenario/01_Background/BG_CS_PV3_54.jpg"
          label="JP"
          href="/jp/"
        >
        </Box>
      </div>
    </main>
  );
}
