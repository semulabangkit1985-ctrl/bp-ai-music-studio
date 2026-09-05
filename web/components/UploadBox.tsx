"use client";

import { useRef, useState } from "react";

interface UploadBoxProps {
  onFileSelected?: (file: File) => void;
}

export default function UploadBox({
  onFileSelected,
}: UploadBoxProps) {
  const inputRef = useRef<HTMLInputElement>(null);
  const [fileName, setFileName] = useState("");
  const [error, setError] = useState("");

  const allowedTypes = [
    "audio/wav",
    "audio/x-wav",
    "audio/mpeg",
    "audio/flac",
    "audio/x-flac",
    "audio/aiff",
    "audio/x-aiff",
    "audio/mp4",
    "audio/x-m4a",
  ];

  function handleFile(file?: File) {
    if (!file) {
      return;
    }

    setError("");

    const extension = file.name
      .split(".")
      .pop()
      ?.toLowerCase();

    const allowedExtensions = [
      "wav",
      "mp3",
      "flac",
      "aiff",
      "aif",
      "m4a",
    ];

    if (
      !allowedTypes.includes(file.type) &&
      !allowedExtensions.includes(extension || "")
    ) {
      setError(
        "Format tidak disokong. Gunakan WAV, MP3, FLAC, AIFF atau M4A."
      );
      return;
    }

    const maxSize =
      500 * 1024 * 1024;

    if (file.size > maxSize) {
      setError(
        "Fail terlalu besar. Saiz maksimum ialah 500 MB."
      );
      return;
    }

    setFileName(file.name);

    if (onFileSelected) {
      onFileSelected(file);
    }
  }

  function handleInputChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    handleFile(event.target.files?.[0]);
  }

  function openFilePicker() {
    inputRef.current?.click();
  }

  return (
    <div className="w-full">
      <input
        ref={inputRef}
        type="file"
        accept=".wav,.mp3,.flac,.aiff,.aif,.m4a,audio/*"
        onChange={handleInputChange}
        className="hidden"
      />

      <button
        type="button"
        onClick={openFilePicker}
        className="flex min-h-56 w-full flex-col items-center justify-center rounded-sonic border border-dashed border-white/20 bg-white/[0.03] p-8 text-center transition hover:border-sonic-400 hover:bg-white/[0.06]"
      >
        <div className="mb-4 text-5xl">
          🎧
        </div>

        <span className="text-lg font-semibold">
          {fileName || "Select your audio"}
        </span>

        <span className="mt-2 text-sm text-gray-500">
          Tap here to choose your music
        </span>

        <span className="mt-4 text-xs text-gray-600">
          WAV • MP3 • FLAC • AIFF • M4A
        </span>
      </button>

      {error && (
        <div className="mt-4 rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-sm text-red-300">
          {error}
        </div>
      )}

      {fileName && !error && (
        <div className="mt-4 rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3 text-sm text-gray-300">
          ✓ Audio selected and ready for mastering.
        </div>
      )}
    </div>
  );
}
