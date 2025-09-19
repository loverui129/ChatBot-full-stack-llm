import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL?.replace(/\/$/, "") || "http://localhost:8000";

export async function askQuestion(question: string) {
  const response = await axios.post(`${API_URL}/ask/`, { question });
  return response.data.answer;
}
