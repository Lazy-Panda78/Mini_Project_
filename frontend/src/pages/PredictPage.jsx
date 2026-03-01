/**
 * PredictPage — drag-and-drop image upload + freshness result display
 * TODO: Connect to backend /predict endpoint
 */
import { useState } from "react";

export default function PredictPage() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (!file) return;
    setLoading(true);
    // TODO: build FormData, POST to API_URL/predict, setResult(data)
    setLoading(false);
  };

  return (
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Food Freshness Classifier</h1>
      {/* TODO: add drag-drop zone, sensor sliders, result card */}
      <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handlePredict} disabled={loading} className="mt-4 px-6 py-2 bg-blue-600 text-white rounded">
        {loading ? "Analyzing..." : "Classify"}
      </button>
      {result && <pre className="mt-4 p-4 bg-gray-100 rounded">{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
