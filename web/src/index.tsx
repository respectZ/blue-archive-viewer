import { render } from "solid-js/web";
import "@fontsource/inter/latin-400.css";
import "@fontsource/inter/latin-700.css";
import { AppRouter } from "./router";
import "./index.css";

const root = document.getElementById("root");
if (!root) throw new Error("Root element #root not found");

render(() => <AppRouter />, root);
