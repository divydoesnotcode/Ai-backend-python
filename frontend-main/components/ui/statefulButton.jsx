"use client";

import React from "react";
import { Button } from "./stateful-button";

export function StatefulButtonDemo() {
  // dummy API call
  const handleClick = () => {
    return new Promise((resolve) => {
      setTimeout(resolve, 4000);
    });
  };
  return (
    <div className="flex w-full items-center justify-center pb-20">
      <Button onClick={handleClick}>Send message</Button>
    </div>
  );
}
