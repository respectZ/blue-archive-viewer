import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Blue Archive",
  description: "Blue Archive Resource Viewer",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <main className="w-full h-full flex flex-col">
          <div className="fixed w-full h-full bg-black opacity-20 -z-10"></div>
          <div
            className="fixed w-full h-full bg-cover bg-center blur-sm -z-20"
            style={{ backgroundImage: "url('/data/jp/MediaResources/UIs/03_Scenario/01_Background/BG_CS_PR_01.jpg')" }}
          >
          </div>
          {children}
        </main>
      </body>
    </html>
  );
}
