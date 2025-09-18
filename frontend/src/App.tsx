import { useState } from "react";
import { askQuestion } from "./ask"; 
import { uploadFile } from "./upload";

function App() {
  const [question, setQuestion] = useState(""); 
  const [answer, setAnswer] = useState(""); 
  const [file, setFile] = useState<File | null>(null);

  const handleAsk = async () => {
    if (!question.trim()) return;
    try {
      const result = await askQuestion(question);
      setAnswer(result);
    } catch (error) {
      console.error(error);
      setAnswer("Error: Failed to fetch answer from backend.");
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    try {
      const result = await uploadFile(file);
      setAnswer(result.message || "Upload successful ✅");
    } catch (error) {
      console.error(error);
      setAnswer("Error: Failed to upload file.");
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial",minHeight: "100vh",
      background: "linear-gradient(135deg, #a8e6cf 0%, #764ba2 100%)"}}>
      <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
        <div style={{ fontSize: "80px", marginRight: "20px" }}>🤖</div>
        <h1>Chatbot</h1>
      </div>

      <input
        type="text"
        value={question} 
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask me anything..."
        style={{ width: "300px", marginRight: "10px" }}
      />
      <button onClick={handleAsk}>Ask</button>

      <div style={{ marginTop: "20px" }}>
        <strong>Answer:</strong>
        <p>{answer}</p>
      </div>

      <div style={{ marginTop: "20px" }}>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files ? e.target.files[0] : null)}
      />
      <button onClick={handleUpload} style={{ marginLeft: "10px" }}>
        Upload
      </button>
    </div>
  </div>
 );
}

export default App;