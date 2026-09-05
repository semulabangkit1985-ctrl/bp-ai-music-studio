"use client";

interface Preset {
  id: string;
  name: string;
  description: string;
}

interface PresetSelectorProps {
  value: string;
  onChange: (preset: string) => void;
}

const PRESETS: Preset[] = [
  {
    id: "universal",
    name: "Universal",
    description: "Seimbang & neutral",
  },
  {
    id: "fire",
    name: "Fire",
    description: "Bertenaga & warm",
  },
  {
    id: "clarity",
    name: "Clarity",
    description: "Terang & bersih",
  },
  {
    id: "tape",
    name: "Tape",
    description: "Hangat analog",
  },
  {
    id: "natural",
    name: "Natural",
    description: "Kekalkan karakter asal",
  },
  {
    id: "spatial",
    name: "Spatial",
    description: "Stereo lebih luas",
  },
  {
    id: "cinematic",
    name: "Cinematic",
    description: "Dalam & immersive",
  },
  {
    id: "punch",
    name: "Punch",
    description: "Hentakan lebih kuat",
  },
];

export default function PresetSelector({
  value,
  onChange,
}: PresetSelectorProps) {
  return (
    <div className="w-full">
      <div className="mb-4">
        <h3 className="text-lg font-semibold">
          Mastering Preset
        </h3>

        <p className="mt-1 text-sm text-gray-500">
          Pilih karakter bunyi untuk lagu anda.
        </p>
      </div>

      <div className="grid gap-3 sm:grid-cols-2">
        {PRESETS.map((preset) => {
          const selected =
            value === preset.id;

          return (
            <button
              key={preset.id}
              type="button"
              onClick={() =>
                onChange(preset.id)
              }
              className={`rounded-xl border p-4 text-left transition ${
                selected
                  ? "border-sonic-400 bg-sonic-500/10"
                  : "border-white/10 bg-white/[0.03] hover:bg-white/[0.06]"
              }`}
              aria-pressed={selected}
            >
              <div className="flex items-center justify-between">
                <span className="font-semibold">
                  {preset.name}
                </span>

                {selected && (
                  <span className="text-xs text-sonic-400">
                    SELECTED
                  </span>
                )}
              </div>

              <p className="mt-1 text-xs text-gray-500">
                {preset.description}
              </p>
            </button>
          );
        })}
      </div>
    </div>
  );
}
