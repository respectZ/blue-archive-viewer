export interface WallpaperEngineProject {
  title: string;
  description: string;
  file: string;
  preview: string;
  general: General;
}

export type General = {
  properties: Properties;
};
export type Properties = {
  [key: string]: Property;
};
export type Property = PropertyCombo | PropertySlider | PropertyBoolean;

export enum PropertyType {
  Combo = "combo",
  Slider = "slider",
  Boolean = "bool",
}

export interface PropertyCombo {
  order: number;
  text: string;
  type: PropertyType.Combo;
  value: string;
  options?: ComboOption[];
}

export interface ComboOption {
  label: string;
  value: string;
}

export interface PropertySlider {
  order: number;
  text: string;
  type: PropertyType.Slider;
  value: number;
  min: number;
  max: number;
  step?: number;
  precision?: number;
}

export interface PropertyBoolean {
  order: number;
  text: string;
  type: PropertyType.Boolean;
  value: boolean;
}

export const createProject = () => {
  const project: WallpaperEngineProject = {
    title: "Blue Archive Live2D",
    description: "A live2D wallpaper for Blue Archive.",
    file: "index.html",
    preview: "icon.jpg",
    general: {
      properties: {
        model: <PropertyCombo> {
          order: 1,
          type: PropertyType.Combo,
          text: "Model",
          value: "airi_home",
          // Add options here.
        },
        scale: <PropertySlider> {
          order: 2,
          type: PropertyType.Slider,
          text: "Scale",
          min: 0.1,
          max: 1.5,
          precision: 2,
          step: 0.1,
          value: 0.8,
        },
        play_voice: <PropertyBoolean> {
          order: 3,
          type: PropertyType.Boolean,
          text: "Play Voice",
          value: true,
        },
        voice_volume: <PropertySlider> {
          order: 4,
          type: PropertyType.Slider,
          text: "Voice Volume",
          value: 100,
          min: 0,
          max: 100,
        },
        tap_to_talk: <PropertyBoolean> {
          order: 5,
          type: PropertyType.Boolean,
          text: "Tap to Talk",
          value: false,
        },
        subtitle: <PropertyCombo> {
          order: 6,
          type: PropertyType.Combo,
          text: "Subtitle",
          value: "none",
          options: [
            {
              label: "None",
              value: "none",
            },
            {
              label: "JP",
              value: "jp",
            },
            {
              label: "EN",
              value: "en",
            },
          ],
        },
      },
    },
  };

  return project;
};
