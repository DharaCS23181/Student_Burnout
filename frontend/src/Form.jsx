import { useState } from "react";

export default function Form() {
  const [form, setForm] = useState({
    age: "",
    study_hours: "",
    sleep_hours: "",
    stress_level: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        age: Number(form.age),
        study_hours: Number(form.study_hours),
        sleep_hours: Number(form.sleep_hours),
        stress_level: Number(form.stress_level)
      })
    });

    const data = await res.json();
    console.log("Prediction:", data);

    setResult(data.prediction);
  };

  return (
    <div className="bg-gray-800 p-6 rounded-xl w-96">
      <h1 className="text-xl mb-4">Burnout Predictor</h1>

      <form onSubmit={handleSubmit} className="space-y-3">
        {Object.keys(form).map((key) => (
          <input
            key={key}
            name={key}
            value={form[key]}
            onChange={handleChange}
            placeholder={key}
            className="w-full p-2 text-black rounded"
          />
        ))}

        <button className="bg-blue-500 w-full p-2 rounded">
          Predict
        </button>
      </form>

      {/* ✅ SHOW RESULT HERE */}
      {result !== null && (
        <div className="mt-4 p-3 rounded bg-gray-700 text-center">
          {result === 1 ? (
            <p className="text-red-400 font-semibold">
              ⚠️ High Burnout Risk
            </p>
          ) : (
            <p className="text-green-400 font-semibold">
              ✅ Low Burnout Risk
            </p>
          )}
        </div>
      )}
    </div>
  );
}