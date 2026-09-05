import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "SONIQ MASTER AI",
  description:
    "AI-powered audio mastering with vocal-safe processing.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
