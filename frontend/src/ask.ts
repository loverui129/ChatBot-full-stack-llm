import axios from "axios";

// Remove a possible trailing slash from API_URL
const API_URL = "https://chatbot-full-stack-llm.onrender.com";

/**
 * Send a question to the backend /ask endpoint
 * @param question The user input question
 */
export async function askQuestion(question: string) {
  try {
    // Use /ask (without trailing slash) to avoid 404 issues
    const response = await axios.post(`${API_URL}/ask`, { question });
    return response.data.answer;
  } catch (error) {
    console.error("Failed to fetch answer from backend:", error);
    throw error;
  }
}
