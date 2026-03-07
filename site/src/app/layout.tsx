import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Investment Intelligence — Analytical Infrastructure for Humans and Agents",
  description:
    "Investment analytical infrastructure — a hosted computation engine callable by analysts, tools, and AI agents. Computed sensitivity grids, Monte Carlo simulations, auditable methodology. Free open-source skills + paid Engine API.",
  openGraph: {
    title: "Investment Intelligence",
    description:
      "Analytical infrastructure callable by analysts, tools, and agents. Computed, auditable investment analysis via API.",
    url: "https://investmentintelligence.ai",
    siteName: "Investment Intelligence",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Investment Intelligence",
    description:
      "Investment analytical infrastructure callable by analysts, tools, and agents.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark scroll-smooth">
      <body
        className={`${geistSans.variable} ${geistMono.variable} font-[family-name:var(--font-geist-sans)] antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
