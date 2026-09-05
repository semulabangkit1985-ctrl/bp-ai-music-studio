"use client";

interface LoudnessMeterProps {
  lufs?: number | null;
  peakDb?: number | null;
  targetLufs?: number;
}

function formatValue(
  value: number | null | undefined,
  suffix: string
) {
  if (
    value === null ||
    value === undefined ||
    !Number.isFinite(value)
  ) {
    return "--";
  }

  return `${value.toFixed(1)} ${suffix}`;
}

export default function LoudnessMeter({
  lufs = null,
  peakDb = null,
  targetLufs = -14,
}: LoudnessMeterProps) {
  const currentLufs =
    typeof lufs === "number"
      ? lufs
      : targetLufs;

  const difference =
    currentLufs - targetLufs;

  const percentage = Math.min(
    100,
    Math.max(
      0,
      ((currentLufs + 30) / 25) * 100
    )
  );

  let status = "Balanced";

  if (difference > 1.5) {
    status = "Loud";
  } else if (difference < -1.5) {
    status = "Dynamic";
  }

  return (
    <section className="sonic-card p-5">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="font-semibold">
            Loudness Meter
          </h3>

          <p className="mt-1 text-xs text-gray-500">
            Integrated loudness
          </p>
        </div>

        <span className="rounded-full bg-white/[0.06] px-3 py-1 text-xs text-gray-400">
          {status}
        </span>
      </div>

      <div className="mt-6">
        <div className="flex items-end justify-between">
          <div>
            <span className="text-3xl font-bold">
              {formatValue(lufs, "LUFS")}
            </span>

            <p className="mt-1 text-xs text-gray-500">
              Target: {targetLufs.toFixed(1)} LUFS
            </p>
          </div>

          <div className="text-right">
            <p className="text-xs text-gray-500">
              Peak
            </p>

            <p className="mt-1 font-semibold">
              {formatValue(peakDb, "dBTP")}
            </p>
          </div>
        </div>

        <div className="mt-5 h-3 overflow-hidden rounded-full bg-white/10">
          <div
            className="h-full rounded-full bg-sonic-500 transition-all"
            style={{
              width: `${percentage}%`,
            }}
          />
        </div>

        <div className="mt-2 flex justify-between text-[10px] text-gray-600">
          <span>-30</span>
          <span>-20</span>
          <span>-14</span>
          <span>-10</span>
          <span>-5</span>
        </div>
      </div>

      <div className="mt-6 grid grid-cols-2 gap-3">
        <div className="rounded-xl bg-white/[0.03] p-3">
          <p className="text-xs text-gray-500">
            Difference
          </p>

          <p className="mt-1 font-semibold">
            {difference >= 0 ? "+" : ""}
            {difference.toFixed(1)} dB
          </p>
        </div>

        <div className="rounded-xl bg-white/[0.03] p-3">
          <p className="text-xs text-gray-500">
            Ceiling
          </p>

          <p className="mt-1 font-semibold">
            -1.0 dBTP
          </p>
        </div>
      </div>
    </section>
  );
}
