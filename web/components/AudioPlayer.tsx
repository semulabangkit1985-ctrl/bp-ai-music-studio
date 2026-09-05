"use client";

import { useEffect, useRef, useState } from "react";

interface AudioPlayerProps {
  src?: string;
  title?: string;
}

export default function AudioPlayer({
  src,
  title = "Audio Preview",
}: AudioPlayerProps) {
  const audioRef =
    useRef<HTMLAudioElement>(null);

  const [playing, setPlaying] =
    useState(false);

  const [currentTime, setCurrentTime] =
    useState(0);

  const [duration, setDuration] =
    useState(0);

  useEffect(() => {
    const audio = audioRef.current;

    if (!audio) {
      return;
    }

    const handleTimeUpdate = () => {
      setCurrentTime(audio.currentTime);
    };

    const handleLoadedMetadata = () => {
      setDuration(audio.duration || 0);
    };

    const handleEnded = () => {
      setPlaying(false);
      setCurrentTime(0);
    };

    audio.addEventListener(
      "timeupdate",
      handleTimeUpdate
    );

    audio.addEventListener(
      "loadedmetadata",
      handleLoadedMetadata
    );

    audio.addEventListener(
      "ended",
      handleEnded
    );

    return () => {
      audio.removeEventListener(
        "timeupdate",
        handleTimeUpdate
      );

      audio.removeEventListener(
        "loadedmetadata",
        handleLoadedMetadata
      );

      audio.removeEventListener(
        "ended",
        handleEnded
      );
    };
  }, [src]);

  async function togglePlayback() {
    const audio = audioRef.current;

    if (!audio || !src) {
      return;
    }

    if (audio.paused) {
      await audio.play();
      setPlaying(true);
    } else {
      audio.pause();
      setPlaying(false);
    }
  }

  function handleSeek(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    const audio = audioRef.current;

    if (!audio) {
      return;
    }

    const time = Number(event.target.value);

    audio.currentTime = time;
    setCurrentTime(time);
  }

  function formatTime(seconds: number) {
    if (!Number.isFinite(seconds)) {
      return "00:00";
    }

    const minutes = Math.floor(
      seconds / 60
    );

    const remainingSeconds = Math.floor(
      seconds % 60
    );

    return `${minutes
      .toString()
      .padStart(2, "0")}:${remainingSeconds
      .toString()
      .padStart(2, "0")}`;
  }

  return (
    <section className="sonic-card p-5">
      <audio
        ref={audioRef}
        src={src}
        preload="metadata"
      />

      <div className="flex items-center gap-4">
        <button
          type="button"
          onClick={togglePlayback}
          disabled={!src}
          className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-sonic-600 text-lg transition hover:bg-sonic-500 disabled:cursor-not-allowed disabled:opacity-40"
          aria-label={
            playing ? "Pause audio" : "Play audio"
          }
        >
          {playing ? "Ⅱ" : "▶"}
        </button>

        <div className="min-w-0 flex-1">
          <h3 className="truncate font-semibold">
            {title}
          </h3>

          <p className="mt-1 text-xs text-gray-500">
            {src
              ? "Audio preview ready"
              : "No audio selected"}
          </p>
        </div>

        <div className="text-right text-xs text-gray-500">
          {formatTime(currentTime)}
          {" / "}
          {formatTime(duration)}
        </div>
      </div>

      <div className="mt-5">
        <input
          type="range"
          min="0"
          max={duration || 0}
          step="0.01"
          value={currentTime}
          onChange={handleSeek}
          disabled={!src}
          className="w-full accent-indigo-500 disabled:opacity-30"
          aria-label="Audio progress"
        />
      </div>
    </section>
  );
}
