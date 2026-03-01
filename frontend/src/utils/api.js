/**
 * API helper — centralised fetch wrapper
 * TODO: replace BASE_URL with your deployed backend URL
 */
const BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export async function predictFreshness(file) {
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch(`${BASE_URL}/predict`, { method: "POST", body: formData });
  if (!res.ok) throw new Error("Prediction failed");
  return res.json();
}

export async function getHistory(limit = 20) {
  const res = await fetch(`${BASE_URL}/history?limit=${limit}`);
  return res.json();
}
