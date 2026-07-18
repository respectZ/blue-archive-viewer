import type { ParentComponent } from "solid-js";
import { Router, Route } from "@solidjs/router";
import { Home } from "./pages/Home";
import { EN } from "./pages/EN";
import { ENLive2D } from "./pages/ENLive2D";
import { JP } from "./pages/JP";
import { JPGallery } from "./pages/JPGallery";
import { JPLive2D } from "./pages/JPLive2D";
import { WPEngine } from "./pages/WPEngine";
import { NotFound } from "./pages/NotFound";

const RootLayout: ParentComponent = (props) => {
  return (
    <main class="relative w-full h-full flex flex-col">
      <div
        class="fixed inset-0 -z-20 bg-cover bg-center"
        style={{
          "background-image":
            "url('/data/jp/MediaResources/Prologue/UIs/03_Scenario/01_Background/BG_CS_PR_01.jpg')",
        }}
      />
      <div class="fixed inset-0 -z-10 bg-[var(--bg-base)]/85" />
      <div class="fixed inset-0 -z-10 bg-gradient-to-t from-[var(--bg-base)] via-transparent to-[var(--accent)]/5 pointer-events-none" />
      <div class="fixed inset-0 -z-10 bg-[radial-gradient(circle_at_50%_0%,var(--accent-glow),transparent_50%)] pointer-events-none" />
      {props.children}
    </main>
  );
};

export function AppRouter() {
  return (
    <Router root={RootLayout}>
      <Route path="/" component={Home} />
      <Route path="/en" component={EN} />
      <Route path="/en/live2d" component={ENLive2D} />
      <Route path="/jp" component={JP} />
      <Route path="/jp/gallery" component={JPGallery} />
      <Route path="/jp/live2d" component={JPLive2D} />
      <Route path="/wpengine" component={WPEngine} />
      <Route path="*" component={NotFound} />
    </Router>
  );
}
