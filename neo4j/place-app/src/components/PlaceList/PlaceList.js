// src/components/PlaceList/PlaceList.js
import React from 'react';
import PlaceCard from '../PlaceCard/PlaceCard';

const PlaceList = ({ places }) => {
  // CITS: Let's explicitly log what PlaceList receives
  console.log('[PlaceList.js] Received places prop:', places);

  if (!places || places.length === 0) {
    return <p>No places to display yet. Enter your name above!</p>;
  }

  return (
    <div className="place-list">
      {places.map((placeItem, index) => {
        // CITS: Log each individual item *before* passing to PlaceCard
        console.log('[PlaceList.js] Mapping item:', placeItem);
        return (
          <PlaceCard key={placeItem.city || index} place={placeItem} />
          // Note: using placeItem.city as key. If cities are not unique,
          // it's safer to use a unique ID from your data if available,
          // or just `index` if no stable ID exists.
        );
      })}
    </div>
  );
};

export default PlaceList;