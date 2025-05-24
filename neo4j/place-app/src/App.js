// src/App.js
import React, { useState } from 'react';
import InputForm from './components/InputForm/InputForm';
import PlaceList from './components/PlaceList/PlaceList';
import { getPlaceRecommendations } from './services/PlaceService';
import './assets/styles/App.css'; // Your main stylesheet

function App() {
  const [recommendedPlaces, setRecommendedPlaces] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [currentUser, setCurrentUser] = useState(''); // To display context

  const handleNameSubmit = async (name) => {
    setIsLoading(true);
    setError(null);
    setRecommendedPlaces([]); // Clear previous recommendations
    setCurrentUser(name);     // Set the name of the user for whom we are fetching

    try {
      const apiResponse = await getPlaceRecommendations(name);
      // Your FastAPI returns an object: { user: "...", recommendations: [...] }
      // We need to set the 'recommendations' array to our state
      setRecommendedPlaces(apiResponse.recommendations || []);
    } catch (err) {
      setError(err.message || 'Could not fetch recommendations.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🏙️ City Recommender</h1>
        <p>Find your next adventure based on users with similar tastes!</p>
      </header>
      <main>
        <InputForm onNameSubmit={handleNameSubmit} />
        {isLoading && <p className="loading-message">Fetching recommendations for <strong>{currentUser}</strong>... ⏳</p>}
        {error && <p className="error-message">Error: {error}</p>}
        {!isLoading && !error && currentUser && recommendedPlaces.length === 0 && (
          <p>No recommendations found for <strong>{currentUser}</strong>. Try a different name or check if the user exists.</p>
        )}
        {/* Pass the actual list of places (recommendations) to PlaceList */}
        <PlaceList places={recommendedPlaces} />
      </main>
      <footer className="App-footer">
        <p>&copy; {new Date().getFullYear()} Your Fancy City Finder</p>
      </footer>
    </div>
  );
}

export default App;