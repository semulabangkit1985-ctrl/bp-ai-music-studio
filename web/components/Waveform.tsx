"use client";

import { useEffect, useRef } from "react";

interface WaveformProps {
  audioUrl?: string;
  height?: number;
}

export default function Waveform({
  audioUrl,
  height = 120,
}: WaveformProps) {
  const canvasRef =
    useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;

    if (!canvas) {
      return;
    }

    const context =
      canvas.getContext("2d");

    if (!context) {
      return;
    }

    const width = canvas.clientWidth;
    const pixelRatio =
      window.devicePixelRatio || 1;

    canvas.width =
      width * pixelRatio;

    canvas.height =
      height * pixelRatio;

    context.scale(
      pixelRatio,
      pixelRatio
    );

    context.clearRect(
      0,
      0,
      width,
      height
    );

    const bars = Math.max(
      40,
      Math.floor(width / 6)
    );

    const center = height / 2;

    for (let i = 0; i < bars; i++) {
      const progress =
        i / bars;

      const wave =
        Math.sin(progress * Math.PI * 12) *
        0.25;

      const variation =
        0.35 +
        Math.abs(
          Math.sin(progress * Math.PI * 5)
        ) *
          0.55;

      const amplitude =
        height *
        0.38 *
        variation *
        (0.75 + wave);

      const x =
        (i / bars) * width;

      const barWidth =
        Math.max(
          2,
          width / bars - 2
        );

      const top =
        center - amplitude;

      const barHeight =
        amplitude * 2;

      context.fillStyle =
        "rgba(96, 117, 255, 0.75)";

      context.beginPath();

      context.roundRect(
        x,
        top,
        barWidth,
        barHeight,
        3
      );

      context.fill();
    }
  }, [height, audioUrl]);

  return (
    <div className="w-full overflow-hidden rounded-xl border border-white/10 bg-white/[0.03]">
      <canvas
        ref={canvasRef}
        style={{
          width: "100%",
          height: `${height}px`,
          display: "block",
        }}
        aria-label="Audio waveform"
      />

      {!audioUrl && (
        <div className="px-4 pb-3 text-center text-xs text-gray-600">
          Waveform preview
        </div>
      )}
    </div>
  );
}
