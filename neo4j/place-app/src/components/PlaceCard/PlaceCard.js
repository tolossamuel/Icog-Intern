// src/components/PlaceCard/PlaceCard.js (or .jsx)
import React from 'react';
// Optional: import './PlaceCard.module.css';

const PlaceCard = ({ place }) => {
  // CITS: Log the 'place' prop received by PlaceCard
  console.log('[PlaceCard.js] Place received:', place);

  if (!place) {
      console.log('[PlaceCard.js] No place data.');
      return null; // Or a fallback message
  }

  return (
    <div className="place-card"> {/* Add a class for styling */}
      {/* CRITICAL: Ensure you are accessing the correct properties */}
      <h3>{place.city}</h3> {/* Is it .city, .name, .title? */}
      {place.country && <p>Country: {place.country}</p>}
      {place.reason && <p>Reason: {place.reason}</p>}
      {place.score && <p>Score: {place.score}</p>} {/* Render the score */}
      {/* Add other relevant properties you expect */}
    </div>
  );
};

export default PlaceCard;