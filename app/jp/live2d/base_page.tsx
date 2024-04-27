"use client";

import InputCheckbox from "@/app/component/input_chekcbox";
import InputSelect from "@/app/component/input_select";
import { createRef, useEffect, useRef } from "react";
import { Live2DViewer } from "@/app/lib/live2d_viewer";
import { fetchModels } from "./model";
import * as Table from "@/app/lib/table";
import { get_origin } from "@/app/lib/get_origin";

import * as events from "./events";
import InputNumber from "@/app/component/input_number";
import Accordion from "@/app/component/accordion";
import Button from "@/app/component/button";
import Modal from "@/app/component/modal";
import ProgressBar from "@/app/component/progress_bar";

var elements: events.Elements = {};

var live2d: Live2DViewer;

interface HomeProps {
  region: "jp" | "en";
}

export const Live2DPage: React.FC<HomeProps> = ({ region }) => {
  const jsonData = createRef<HTMLAnchorElement>();
  const settingPanel = createRef<HTMLDivElement>();
  const subtitle = createRef<HTMLDivElement>();
  const animationSelect = createRef<HTMLSelectElement>();
  const modelSelect = createRef<HTMLSelectElement>();
  const loopAnimation = createRef<HTMLInputElement>();
  const playVoice = createRef<HTMLInputElement>();
  const playBGM = createRef<HTMLInputElement>();
  const scale = createRef<HTMLInputElement>();
  const offsetX = createRef<HTMLInputElement>();
  const offsetY = createRef<HTMLInputElement>();
  const audioBGM = createRef<HTMLAudioElement>();
  const exportBitrate = createRef<HTMLInputElement>();
  const exportFPS = createRef<HTMLInputElement>();
  const modal = createRef<HTMLDivElement>();
  const progressBar = createRef<HTMLDivElement>();
  const modalClose = createRef<HTMLButtonElement>();

  useEffect(() => {
    if (settingPanel.current) elements.settingPanel = settingPanel.current;
    if (subtitle.current) elements.subtitle = subtitle.current;
    if (animationSelect.current) elements.animationSelect = animationSelect.current;
    if (modelSelect.current) elements.modelSelect = modelSelect.current;
    if (loopAnimation.current) elements.loopAnimation = loopAnimation.current;
    if (playVoice.current) elements.playVoice = playVoice.current;
    if (playBGM.current) elements.playBGM = playBGM.current;
    if (scale.current) elements.scale = scale.current;
    if (offsetX.current) elements.offsetX = offsetX.current;
    if (offsetY.current) elements.offsetY = offsetY.current;
    if (jsonData.current) elements.jsonData = jsonData.current;
    if (audioBGM.current) elements.audioBGM = audioBGM.current;
    if (exportBitrate.current) elements.exportBitrate = exportBitrate.current;
    if (exportFPS.current) elements.exportFPS = exportFPS.current;
    if (modal.current) elements.modal = modal.current;
    if (progressBar.current) elements.progressBar = progressBar.current;
    if (modalClose.current) elements.modalClose = modalClose.current;

    live2d = new Live2DViewer(document.querySelector("canvas")!);

    Table.initialize(region).then(() => {
      fetchModels(elements.jsonData!.href).then(async (models) => {
        document.getElementById("loading")!.classList.add("opacity-0");
        document.getElementById("loading")!.classList.remove("opacity-100");
        setTimeout(() => {
          document.getElementById("loading")!.remove();
        }, 1000);

        // Update models value by adding origin
        const origin = get_origin();
        for (const [key, value] of Object.entries(models)) {
          models[key] = value.map((v) => origin + "/" + v);
        }
        events.ReloadModels(elements.modelSelect!, models, region === "en"); // sort only for en
        events.LoadModel(elements, live2d);
        events.EnableDragging(elements, live2d);
      });
    });

    window.addEventListener("resize", (e) => events.OnResize(e, elements, live2d));
  });

  return (
    <main className="h-full w-full font-sans">
      {/* Modal */}
      <Modal reference={modal} className="hidden">
        <div className="flex flex-col w-full xl:w-96">
          <p className="text-2xl mb-4">Exporting...</p>
          <ProgressBar className="grow mb-4" height={2} percent={0} reference={progressBar}></ProgressBar>
          <video controls className="mb-4"></video>
          <Button
            id="modal-close"
            label="Close"
            reference={modalClose}
            onClick={() => {
              modal.current!.classList.add("hidden");
            }}
          />
        </div>
      </Modal>
      {/* Loading */}
      <div className="w-screen h-screen fixed flex items-center justify-center z-50 bg-neutral-800 bg-opacity-80 transition-all duration-1000 opacity-100" id="loading">
        <p className="text-2xl text-gray-100">Loading...</p>
      </div>
      <a href="/data/jp/Android/info.json" className="hidden" id="jsonData" ref={jsonData}></a>
      {/* Settings button */}
      <div className="w-24 h-12 fixed">
        <button
          className="w-full h-full flex justify-center items-center border-2 border-gray-400"
          id="setting-button"
          onClick={() => events.OpenSetting(elements.settingPanel!)}
        >
          <span uk-icon="cog" className="uk-icon">
            <svg
              width="20"
              height="20"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <circle fill="none" stroke="#fff" cx="9.997" cy="10" r="3.31">
              </circle>
              <path
                fill="none"
                stroke="#fff"
                d="M18.488,12.285 L16.205,16.237 C15.322,15.496 14.185,15.281 13.303,15.791 C12.428,16.289 12.047,17.373 12.246,18.5 L7.735,18.5 C7.938,17.374 7.553,16.299 6.684,15.791 C5.801,15.27 4.655,15.492 3.773,16.237 L1.5,12.285 C2.573,11.871 3.317,10.999 3.317,9.991 C3.305,8.98 2.573,8.121 1.5,7.716 L3.765,3.784 C4.645,4.516 5.794,4.738 6.687,4.232 C7.555,3.722 7.939,2.637 7.735,1.5 L12.263,1.5 C12.072,2.637 12.441,3.71 13.314,4.22 C14.206,4.73 15.343,4.516 16.225,3.794 L18.487,7.714 C17.404,8.117 16.661,8.988 16.67,10.009 C16.672,11.018 17.415,11.88 18.488,12.285 L18.488,12.285 Z"
              >
              </path>
            </svg>
          </span>
        </button>
      </div>

      <div
        className="xl:w-96 w-full h-screen bg-neutral-800 pt-6 px-12 fixed duration-300 left-0 z-10 overflow-y-auto"
        id="setting"
        ref={settingPanel}
      >
        <div className="flex flex-row justify-end text-gray-100">
          <svg
            width="16"
            height="16"
            viewBox="0 0 14 14"
            xmlns="http://www.w3.org/2000/svg"
            className="cursor-pointer"
            id="close"
            onClick={() => events.CloseSetting(elements.settingPanel!)}
          >
            <line
              fill="none"
              stroke="#fff"
              strokeWidth="1.1"
              x1="1"
              y1="1"
              x2="13"
              y2="13"
            >
            </line>
            <line
              fill="none"
              stroke="#fff"
              strokeWidth="1.1"
              x1="13"
              y1="1"
              x2="1"
              y2="13"
            >
            </line>
          </svg>
        </div>

        <div className="flex flex-col pt-6 pb-12 text-gray-400">
          <p className="text-4xl text-gray-100">Settings</p>

          <InputSelect
            id="model"
            label="Model"
            onChange={() => {
              events.LoadModel(elements, live2d);
            }}
            options={[]}
            reference={modelSelect}
          />

          <InputSelect
            id="animation"
            label="Animation"
            onChange={() => {
              events.AnimationOnChanged(elements, live2d);
            }}
            options={[]}
            reference={animationSelect}
          />

          <br />

          <InputCheckbox
            id="loop-animation"
            label="Loop animation"
            onChange={() => {
              live2d.loopAnimation = loopAnimation.current!.checked;
            }}
            reference={loopAnimation}
          />

          <InputCheckbox
            id="play-voice"
            label="Play voice"
            onChange={() => events.PlayVoiceOnChanged(playVoice.current!.checked, live2d)}
            reference={playVoice}
          />

          <InputCheckbox
            id="play-bgm"
            label="Play BGM"
            onChange={() => {
              events.ReloadBGM(elements);
            }}
            reference={playBGM}
          />

          <br />

          <audio src="" preload="auto" ref={audioBGM} loop controls hidden></audio>

          <br />

          <Button
            id="download"
            label="Download as Wallpaper Engine Web"
            onClick={() => {
              events.DownloadAsWallpaperEngine(elements);
            }}
          />

          <br />

          <Accordion title="Extras">
            <p className="text-xl text-gray-200 mb-2">Scale</p>

            <div className="flex flex-row">
              <Button
                id="scale-fill"
                label="Fill"
                onClick={() => {
                  events.ScaleFill(elements, live2d);
                }}
              />
              <Button
                id="scale-fit"
                label="Fit"
                onClick={() => {
                  events.ScaleFit(elements, live2d);
                }}
              />
            </div>

            <InputNumber
              id="scale-x"
              label="X"
              onChange={() => {
                events.ScaleChanged(elements, live2d);
              }}
              reference={scale}
              min={0.1}
              max={20}
              step={0.1}
            />

            <br />

            <p className="text-xl text-gray-200 mb-2">Offset</p>

            <div className="flex flex-row">
              <Button
                id="offset-center"
                label="Center"
                onClick={() => {
                  events.OffsetCenter(elements, live2d);
                }}
              />
            </div>

            <p className="mb-2">You can also move by dragging it.</p>

            <InputNumber
              id="offset-x"
              label="X"
              onChange={() => {
                events.OffsetChanged(elements, live2d);
              }}
              reference={offsetX}
              min={-1920}
              max={1920}
              step={1}
            />

            <InputNumber
              id="offset-y"
              label="Y"
              onChange={() => {
                events.OffsetChanged(elements, live2d);
              }}
              reference={offsetY}
              min={-1080}
              max={1080}
              step={1}
            />
            <br />
          </Accordion>
          <br />
          <Accordion title="Export">
            <div className="flex flex-col">
              <InputNumber
                id="export-bitrate"
                label="Bitrate (Mbps)"
                min={5}
                max={100}
                step={1}
                reference={exportBitrate}
              />

              <InputNumber
                id="export-fps"
                label="FPS "
                defaultValue={30}
                min={1}
                max={60}
                step={1}
                reference={exportFPS}
              />
            </div>
            <br />
            <Button
              id="export-button"
              label="Go!"
              onClick={async () => await events.ExportAs(elements, live2d)}
            />
          </Accordion>
        </div>
      </div>

      <div className="w-full h-full flex items-center justify-center">
        <canvas
          id="canvas"
          onClick={() => events.CloseSetting(elements.settingPanel!)}
        >
        </canvas>
      </div>
      {/* Footer */}
      <div className="w-screen h-12 fixed bottom-0 flex justify-center items-center bg-neutral-800">
        <p className="text-gray-400">Live2D Viewer</p>
      </div>
      <div className="sm:w-full xl:w-auto h-auto fixed bottom-24 flex flex-col xl:px-96" ref={subtitle}>
      </div>
    </main>
  );
};
