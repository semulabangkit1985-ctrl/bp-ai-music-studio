"use client";

import { useState } from "react";

const presets = [
  "Universal",
  "Fire",
  "Clarity",
  "Tape",
  "Natural",
  "Spatial",
  "Cinematic",
  "Punch",
];

export default function StudioPage() {
  const [fileName, setFileName] = useState("");
  const [preset, setPreset] = useState("Universal");
  const [targetLufs, setTargetLufs] = useState("-14");
  const [vocalSafe, setVocalSafe] = useState(true);
  const [status, setStatus] = useState("");

  function handleFileChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    setFileName(file.name);
    setStatus("Audio selected. Ready for analysis.");
  }

  function handleMaster() {
    if (!fileName) {
      setStatus("Please select an audio file first.");
      return;
    }

    setStatus(
      `Mastering ready • ${preset} • ${targetLufs} LUFS`
    );
  }

  return (
    <main className="min-h-screen bg-black px-5 py-8 text-white sm:px-8">
      <div className="mx-auto max-w-6xl">
        <header className="mb-10 flex flex-col gap-3">
          <p className="text-sm font-medium uppercase tracking-[0.25em] text-sonic-400">
            SONIQ MASTER AI
          </p>

          <h1 className="text-3xl font-bold sm:text-5xl">
            Mastering Studio
          </h1>

          <p className="max-w-2xl text-gray-400">
            Upload muzik anda dan biarkan SONIQ MASTER AI
            menyediakan mastering yang seimbang sambil
            melindungi karakter vokal asal.
          </p>
        </header>

        <div className="grid gap-6 lg:grid-cols-[1.4fr_0.8fr]">
          <section className="sonic-card p-6 sm:p-8">
            <div className="mb-6">
              <h2 className="text-xl font-semibold">
                Audio Input
              </h2>

              <p className="mt-2 text-sm text-gray-400">
                WAV, MP3, FLAC, AIFF atau M4A
              </p>
            </div>

            <label className="flex min-h-64 cursor-pointer flex-col items-center justify-center rounded-sonic border border-dashed border-white/20 bg-white/[0.03] p-8 text-center transition hover:bg-white/[0.06]">
              <div className="mb-4 text-5xl">
                🎵
              </div>

              <span className="text-lg font-semibold">
                {fileName || "Upload your track"}
              </span>

              <span className="mt-2 text-sm text-gray-500">
                Tap to select an audio file
              </span>

              <input
                type="file"
                accept=".wav,.mp3,.flac,.aiff,.aif,.m4a,audio/*"
                onChange={handleFileChange}
                className="hidden"
              />
            </label>

            {status && (
              <div className="mt-5 rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3 text-sm text-gray-300">
                {status}
              </div>
            )}

            <div className="mt-8 grid gap-4 sm:grid-cols-3">
              <div className="rounded-xl bg-white/[0.04] p-4">
                <p className="text-xs text-gray-500">
                  Analysis
                </p>
                <p className="mt-1 font-semibold">
                  AI Ready
                </p>
              </div>

              <div className="rounded-xl bg-white/[0.04] p-4">
                <p className="text-xs text-gray-500">
                  Vocal Protection
                </p>
                <p className="mt-1 font-semibold">
                  {vocalSafe ? "Enabled" : "Disabled"}
                </p>
              </div>

              <div className="rounded-xl bg-white/[0.04] p-4">
                <p className="text-xs text-gray-500">
                  Output Ceiling
                </p>
                <p className="mt-1 font-semibold">
                  -1.0 dBTP
                </p>
              </div>
            </div>
          </section>

          <aside className="sonic-card p-6 sm:p-8">
            <h2 className="text-xl font-semibold">
              Mastering Settings
            </h2>

            <div className="mt-6">
              <label className="text-sm text-gray-400">
                Preset
              </label>

              <select
                value={preset}
                onChange={(event) =>
                  setPreset(event.target.value)
                }
                className="mt-2 w-full rounded-xl border border-white/10 bg-white/[0.05] px-4 py-3 outline-none focus:border-sonic-400"
              >
                {presets.map((item) => (
                  <option
                    key={item}
                    value={item}
                    className="bg-black"
                  >
                    {item}
                  </option>
                ))}
              </select>
            </div>

            <div className="mt-6">
              <label className="text-sm text-gray-400">
                Target Loudness
              </label>

              <select
                value={targetLufs}
                onChange={(event) =>
                  setTargetLufs(event.target.value)
                }
                className="mt-2 w-full rounded-xl border border-white/10 bg-white/[0.05] px-4 py-3 outline-none focus:border-sonic-400"
              >
                <option value="-16">-16 LUFS</option>
                <option value="-14">-14 LUFS</option>
                <option value="-12">-12 LUFS</option>
                <option value="-10">-10 LUFS</option>
              </select>
            </div>

            <div className="mt-6 rounded-xl border border-white/10 bg-white/[0.03] p-4">
              <div className="flex items-center justify-between gap-4">
                <div>
                  <p className="font-semibold">
                    Vocal Safe
                  </p>

                  <p className="mt-1 text-xs leading-5 text-gray-500">
                    Melindungi pitch, formant dan identiti
                    vokal asal.
                  </p>
                </div>

                <button
                  type="button"
                  onClick={() =>
                    setVocalSafe(!vocalSafe)
                  }
                  aria-pressed={vocalSafe}
                  className={`h-7 w-12 rounded-full p-1 transition ${
                    vocalSafe
                      ? "bg-sonic-600"
                      : "bg-white/20"
                  }`}
                >
                  <span
                    className={`block h-5 w-5 rounded-full bg-white transition ${
                      vocalSafe
                        ? "translate-x-5"
                        : "translate-x-0"
                    }`}
                  />
                </button>
              </div>
            </div>

            <button
              type="button"
              onClick={handleMaster}
              className="sonic-button mt-8 w-full"
            >
              Start AI Mastering
            </button>

            <p className="mt-4 text-center text-xs leading-5 text-gray-500">
              SONIQ Master AI akan menganalisis audio
              sebelum pemprosesan akhir.
            </p>
          </aside>
        </div>
      </div>
    </main>
  );
}
