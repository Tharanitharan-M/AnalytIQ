const API = process.env.NEXT_PUBLIC_API_URL;

export async function pingBackend() {
  const res = await fetch(`${API}/health`, { cache: "no-store" });
  return res.json();
}

export async function listDatasets() {
  const res = await fetch(`${API}/catalog/list`, { cache: "no-store" });
  return res.json();
}