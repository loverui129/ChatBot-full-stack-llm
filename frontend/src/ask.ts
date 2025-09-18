import axios from "axios";

const API_URL = "http://localhost:8000";

export async function askQuestion(question: string) {
  const response = await axios.post(`${API_URL}/ask/`, { question });
  return response.data.answer;
}
