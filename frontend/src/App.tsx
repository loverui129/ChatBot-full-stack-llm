import { useState } from "react";
import { askQuestion } from "./chat"; // API call for chatbot questions
import { uploadFile } from "./upload"; // API call for file upload   


function App() {     
  //  React state hooks 组件记住数据、响应生命周期事件 
  const [question, setQuestion] = useState("");   // User input
  const [answer, setAnswer] = useState(""); // AI response
  const [file, setFile] = useState<File | null>(null); // Selected file

   // Send user's question to backend /chat endpoint
  const handleAsk = async () => {  // 异步函数
    if (!question.trim()) return; // trim:去除空格,如果输入为空,则返回
    try {  //  异步错误处理
      const result = await askQuestion(question); // API call:后端返回的数据
      setAnswer(result);
    } catch (error) {
      console.error(error);
      setAnswer("Error: Failed to fetch answer from backend."); // 显示错误信息,用户可以看到的,如果失败了
    }
  };
 
  // Upload a file to backend /upload endpoint
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
    <div style={{ padding: "40px", fontFamily: "Arial",minHeight: "100vh", 
      display: "flex",flexDirection: "column",alignItems: "center",justifyContent: "center",background: "transparent", //内联样式（inline style）
}}>
      <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
        <div style={{ fontSize: "80px", marginRight: "20px" }}>🤖</div>
        <h1>Chatbot</h1>
      </div>

      <input
        type="text" // event handler: onChange 事件处理器
        value={question} //Controlled Component 受控：由 React 的 state 控制
        onChange={(e) => setQuestion(e.target.value)} //事件绑定（onChange）:输入框的值发生变化时触发 + 状态更新（setState）
        placeholder="Ask me anything..."
        style={{ width: "300px", marginRight: "10px" }}
         // on Click:triggerd by 客人点击按钮
      /> 
      <button
        onClick={handleAsk}
        style={{
          marginLeft: "10px",
          borderRadius: "8px",
          padding: "8px 16px",
          border: "none",
          backgroundColor: "#4a69bd",
          color: "white",
          cursor: "pointer",
          transition: "background-color 0.3s",
        }}
        onMouseOver={(e) => (e.currentTarget.style.backgroundColor = "#6a89cc")}
        onMouseOut={(e) => (e.currentTarget.style.backgroundColor = "#4a69bd")}
>
  Ask
</button> 
      
      <div style={{ marginTop: "20px" }}>
        <strong>Answer:</strong>
        <p>{answer}</p>     
      </div>
      
      <div style={{ marginTop: "20px" }}> 
      <input
        type="file" // event handler: onChange 事件处理器
        onChange={(e) => setFile(e.target.files ? e.target.files[0] : null)}  // 状态更新（setState）,存储文件到state
      />
      <button
        onClick={handleUpload}
        style={{
          marginLeft: "10px",
          borderRadius: "8px",
          padding: "8px 16px",
          border: "none",
          backgroundColor: "#20bf6b",
          color: "white",
          cursor: "pointer",
          transition: "background-color 0.3s",
        }}
        onMouseOver={(e) => (e.currentTarget.style.backgroundColor = "#26de81")}
        onMouseOut={(e) => (e.currentTarget.style.backgroundColor = "#20bf6b")}
      >
  Upload
</button>

    </div>
  </div>
 );
}

export default App;