import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setPrediction(`Empty: ${data.empty}, Occupied: ${data.occupied}`);
    } catch (error) {
      console.error(error);
      setPrediction("Error occurred");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Parking Detection App</h1>

      {/* FILE INPUT */}
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      {/* BUTTON */}
      <button onClick={handleUpload}>
        Upload & Predict
      </button>

      <h2>{prediction}</h2>
    </div>
  );
}

export default App;