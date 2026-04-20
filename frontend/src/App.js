import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [image, setImage] = useState("");
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

      console.log("Backend Response:", data);

      if (data.error) {
        setPrediction("Error: " + data.error);
        return;
      }

      // Show image
      setImage(`data:image/jpeg;base64,${data.image}`);

      // Show counts
      setPrediction(`Empty: ${data.empty}, Occupied: ${data.occupied}`);

    } catch (error) {
      console.error(error);
      setPrediction("Server error");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Parking Detection App</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>
        Upload & Predict
      </button>

      <h2>{prediction}</h2>

      {/* SHOW IMAGE */}
      {image && (
        <img
          src={image}
          alt="Detected Parking"
          style={{ marginTop: "20px", width: "500px", border: "2px solid black" }}
        />
      )}
    </div>
  );
}

export default App;

// import React, { useState } from "react";

// function App() {
//   const [file, setFile] = useState(null);
//   const [prediction, setPrediction] = useState("");

//   const handleUpload = async () => {
//     if (!file) {
//       alert("Please select an image");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);

//     try {
//       const response = await fetch("http://127.0.0.1:5000/predict", {
//         method: "POST",
//         body: formData,
//       });

//       const data = await response.json();
//       setPrediction(`Empty: ${data.empty}, Occupied: ${data.occupied}`);
//     } catch (error) {
//       console.error(error);
//       setPrediction("Error occurred");
//     }
//   };

//   return (
//     <div style={{ textAlign: "center", marginTop: "50px" }}>
//       <h1>Parking Detection App</h1>

//       {/* FILE INPUT */}
//       <input
//         type="file"
//         onChange={(e) => setFile(e.target.files[0])}
//       />

//       <br /><br />

//       {/* BUTTON */}
//       <button onClick={handleUpload}>
//         Upload & Predict
//       </button>

//       <h2>{prediction}</h2>
//     </div>
//   );
// }

// export default App;
