    import axios from "axios"; // Axios for frontend HTTP requests

    const API_URL = import.meta.env.VITE_API_URL;

    // Upload file to backend /upload endpoint
    export async function uploadFile(file: File) {  
        const formData = new FormData(); // Create a FormData object
        formData.append("file", file); // Append file to formData
        const response = await axios.post(`${API_URL}/upload/`, formData, {
            headers: { "Content-Type": "multipart/form-data" },
          });
        
        return response.data;
    }

