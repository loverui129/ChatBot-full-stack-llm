    import axios from "axios"; // Axios for frontend HTTP requests

    const API_URL = "http://127.0.0.1:8000";

    // Upload file to backend /upload endpoint
    export async function uploadFile(file: File) {  
        const formData = new FormData(); // Create a FormData object
        formData.append("file", file); // Append file to formData
        const response = await axios.post(`${API_URL}/upload/`, formData, {
            headers: { "Content-Type": "multipart/form-data" },
          });
        
        return response.data;
    }

