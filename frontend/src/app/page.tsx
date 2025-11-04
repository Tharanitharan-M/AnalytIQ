"use client";
import { useEffect, useState } from "react";
import { pingBackend } from "@/lib/api";

export default function Home() {
  const [status, setStatus] = useState("checking…");
  useEffect(() => {
    pingBackend().then(d => setStatus(JSON.stringify(d))).catch(() => setStatus("failed"));
  }, []);
  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold">AnalytIQ</h1>
      <p className="mt-4">Backend health: {status}</p>
    </main>
  );
}