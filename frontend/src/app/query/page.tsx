"use client";
import ChartView from "@/components/ChartView";
import { useState } from "react";

export default function QueryPage() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState<any>(null);

  async function ask() {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/query/run`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setResult(data);
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-semibold mb-4">Ask your data</h1>
      <div className="flex gap-2">
        <input className="border px-3 py-2 rounded w-96"
               placeholder="e.g. total signups last month"
               value={prompt} onChange={e=>setPrompt(e.target.value)} />
        <button className="bg-blue-600 text-white px-3 py-2 rounded" onClick={ask}>Ask</button>
      </div>
      {result?.rows && (
        <ChartView data={result.rows} xKey="status" yKey="count" /> 
      )}
      {result && (
        <pre className="bg-gray-100 mt-6 p-4 rounded">{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}