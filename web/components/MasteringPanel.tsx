"use client";

import { useState } from "react";

interface MasteringPanelProps {
  fileId?: string;
  onMasteringStarted?: (jobId: string) => void;
}

const presets = [
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

export default function MasteringPanel({
  fileId,
  onMasteringStarted,
}: MasteringPanelProps) {
  const [preset, setPreset] = useState("universal");
  const [targetLufs, setTargetLufs] = useState(-14);
  const [vocalSafe, setVocalSafe] = useState(true);
  const [processing, setProcessing] = useState(false);
  const [message, setMessage] = useState("");

  async function startMastering() {
    if (!fileId) {
      setMessage(
        "Sila upload audio terlebih dahulu."
      );
      return;
    }

    setProcessing(true);
    setMessage(
      "SONIQ MASTER AI sedang menyediakan mastering..."
    );

    try {
      const response = await fetch(
        "/api/mastering",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            file_id: fileId,
            preset,
            target_lufs: targetLufs,
            true_peak_db: -1.0,
            vocal_safe: vocalSafe,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(
          "Mastering request failed."
        );
      }

      const data = await response.json();

      const jobId =
        data.job_id || data.id || "";

      setMessage(
        "Mastering telah dimulakan."
      );

      if (
        jobId &&
        onMasteringStarted
      ) {
        onMasteringStarted(jobId);
      }
    } catch {
      setMessage(
        "Tidak dapat memulakan mastering. Pastikan API sedang berjalan."
      );
    } finally {
      setProcessing(false);
    }
  }

  return (
    <section className="sonic-card p-6">
      <div className="mb-6">
        <h2 className="text-xl font-semibold">
          AI Mastering
        </h2>

        <p className="mt-2 text-sm text-gray-400">
          Pilih karakter mastering yang anda mahu.
        </p>
      </div>

      <div>
        <label className="text-sm font-medium text-gray-300">
          Mastering Preset
        </label>

        <div className="mt-3 grid gap-3 sm:grid-cols-2">
          {presets.map((item) => {
            const selected =
              preset === item.id;

            return (
              <button
                key={item.id}
                type="button"
                onClick={() =>
                  setPreset(item.id)
                }
                className={`rounded-xl border p-4 text-left transition ${
                  selected
                    ? "border-sonic-400 bg-sonic-500/10"
                    : "border-white/10 bg-white/[0.03] hover:bg-white/[0.06]"
                }`}
              >
                <div className="font-semibold">
                  {item.name}
                </div>

                <div className="mt-1 text-xs text-gray-500">
                  {item.description}
                </div>
              </button>
            );
          })}
        </div>
      </div>

      <div className="mt-7">
        <label className="text-sm font-medium text-gray-300">
          Target Loudness
        </label>

        <select
          value={targetLufs}
          onChange={(event) =>
            setTargetLufs(
              Number(event.target.value)
            )
          }
          className="mt-3 w-full rounded-xl border border-white/10 bg-white/[0.05] px-4 py-3 text-white outline-none focus:border-sonic-400"
        >
          <option
            value="-16"
            className="bg-black"
          >
            -16 LUFS — Dynamic
          </option>

          <option
            value="-14"
            className="bg-black"
          >
            -14 LUFS — Balanced
          </option>

          <option
            value="-12"
            className="bg-black"
          >
            -12 LUFS — Loud
          </option>

          <option
            value="-10"
            className="bg-black"
          >
            -10 LUFS — Very Loud
          </option>
        </select>
      </div>

      <div className="mt-6 rounded-xl border border-white/10 bg-white/[0.03] p-4">
        <div className="flex items-center justify-between gap-4">
          <div>
            <h3 className="font-semibold">
              Vocal Safe
            </h3>

            <p className="mt-1 text-xs leading-5 text-gray-500">
              Tiada pitch shift, formant shift,
              voice replacement atau voice cloning.
            </p>
          </div>

          <button
            type="button"
            aria-pressed={vocalSafe}
            onClick={() =>
              setVocalSafe(!vocalSafe)
            }
            className={`relative h-7 w-12 rounded-full p-1 transition ${
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
        disabled={processing}
        onClick={startMastering}
        className="sonic-button mt-7 w-full"
      >
        {processing
          ? "Processing..."
          : "Start AI Mastering"}
      </button>

      {message && (
        <div className="mt-4 rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3 text-sm text-gray-300">
          {message}
        </div>
      )}
    </section>
  );
}
