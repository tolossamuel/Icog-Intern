// src/services/PlaceService.js

// Your FastAPI backend URL (default is http://localhost:8000)
const API_BASE_URL = 'http://0.0.0.0:5000';

export const getPlaceRecommendations = async (userName) => {
  try {
    const response = await fetch(`${API_BASE_URL}/recommendations`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      // Ensure the body matches what your FastAPI expects: {"user_name": "string"}
      body: JSON.stringify({ user_name: userName }),
    });

    if (!response.ok) {
      // Try to parse error detail from FastAPI
      const errorData = await response.json().catch(() => ({ detail: response.statusText }));
      throw new Error(`API Error: ${response.status} - ${errorData.detail || 'Failed to fetch recommendations'}`);
    }
    return await response.json(); // This will be { user: "...", recommendations: [...] }
  } catch (error) {
    console.error("Failed to fetch place recommendations:", error);
    // Re-throw the error so the component can catch it
    throw error;
  }
};