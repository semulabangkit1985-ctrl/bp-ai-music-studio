import Link from "next/link";

const features = [
  {
    title: "AI Audio Analysis",
    description:
      "Analisis loudness, peak, dynamics dan karakter audio sebelum mastering.",
  },
  {
    title: "Vocal Safe",
    description:
      "Melindungi identiti dan karakter suara penyanyi asal.",
  },
  {
    title: "Smart Mastering",
    description:
      "AI memilih pemprosesan yang sesuai berdasarkan kandungan muzik.",
  },
  {
    title: "Studio Presets",
    description:
      "Universal, Fire, Clarity, Tape, Natural, Spatial, Cinematic dan Punch.",
  },
];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-black text-white">
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-b from-sonic-900/30 via-black to-black" />

        <div className="relative mx-auto flex min-h-screen max-w-6xl flex-col items-center justify-center px-6 py-20 text-center">
          <div className="mb-6 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-gray-300">
            AI AUDIO MASTERING STUDIO
          </div>

          <h1 className="max-w-4xl text-5xl font-bold tracking-tight sm:text-7xl">
            SONIQ{" "}
            <span className="text-sonic-400">
              MASTER AI
            </span>
          </h1>

          <p className="mt-6 max-w-2xl text-lg leading-8 text-gray-400">
            Professional AI mastering untuk menghasilkan bunyi
            yang lebih jelas, seimbang, bertenaga dan tetap
            mengekalkan karakter vokal asal.
          </p>

          <div className="mt-10 flex flex-col gap-4 sm:flex-row">
            <Link
              href="/studio"
              className="rounded-sonic bg-sonic-600 px-8 py-4 font-semibold transition hover:bg-sonic-500"
            >
              Open Mastering Studio
            </Link>

            <a
              href="#features"
              className="rounded-sonic border border-white/15 bg-white/5 px-8 py-4 font-semibold transition hover:bg-white/10"
            >
              Explore Features
            </a>
          </div>

          <div
            id="features"
            className="mt-24 grid w-full gap-5 text-left sm:grid-cols-2 lg:grid-cols-4"
          >
            {features.map((feature) => (
              <div
                key={feature.title}
                className="rounded-sonic border border-white/10 bg-white/[0.04] p-6 shadow-sonic backdrop-blur"
              >
                <h2 className="text-lg font-semibold">
                  {feature.title}
                </h2>

                <p className="mt-3 text-sm leading-6 text-gray-400">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>

          <div className="mt-16 text-sm text-gray-500">
            Vocal Safe • Transparent Processing • Studio Ready
          </div>
        </div>
      </section>
    </main>
  );
}
