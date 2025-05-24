import React, { useState } from 'react';
// Optional: import './InputForm.module.css'; // For CSS Modules

const InputForm = ({ onNameSubmit }) => {
  const [name, setName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (name.trim()) {
      onNameSubmit(name);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="input-form"> {/* Add a class for styling */}
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
        aria-label="Name for place recommendations"
      />
      <button type="submit">Get Recommendations</button>
    </form>
  );
};

export default InputForm;