import axios from "axios"; //Frontend uses Axios to call backend API

const API_URL = "http://localhost:8000";


// Send user's question to the backend /chat endpoint
export async function askQuestion(question: string) {
  const response = await axios.post(`${API_URL}/chat/`, { question });
  return response.data.answer;
}
