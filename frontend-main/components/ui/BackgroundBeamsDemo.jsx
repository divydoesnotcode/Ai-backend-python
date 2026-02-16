"use client";
import React from "react";
import { BackgroundBeams } from "../ui/background-beams";

export function BackgroundBeamsDemo() {
  return (
    <div
      className="min-h-screen w-full bg-neutral-950 relative flex flex-col items-center justify-center antialiased overflow-hidden">
      <div className="max-w-2xl mx-auto p-4 md:p-8 relative z-10">
        <p className="text-neutral-500 max-w-lg mx-auto my-4 text-sm md:text-base text-center">
        </p>
      </div>
      <BackgroundBeams />
    </div>
  );
}
