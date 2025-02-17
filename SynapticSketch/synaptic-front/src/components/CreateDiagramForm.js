// src/components/CreateDiagramForm.js
import React, { useState } from 'react';
import axios from 'axios';

function CreateDiagramForm() {
  const [title, setTitle] = useState('');
  const [shapes, setShapes] = useState([]);
  // You could get fancy and have a UI for shapes, but let's keep it simple

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Post to Django's API
      const response = await axios.post('http://127.0.0.1:8000/api/diagrams/', {
        title,
        data: {
          shapes,         // or an empty array
          connections: [], // e.g., empty or some default
        },
      });
      console.log('Created diagram:', response.data);
      // Possibly redirect to a DiagramCanvas page:
      // window.location.href = `/diagram/${response.data.id}`;
    } catch (error) {
      console.error('Error creating diagram:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create a New Diagram</h2>
      <div>
        <label>Title:</label>
        <input
          type="text"
          value={title}
          onChange={e => setTitle(e.target.value)}
        />
      </div>
      {/* If you want to let user define shapes in the form, you'd add more fields */}
      <button type="submit">Create Diagram</button>
    </form>
  );
}

export default CreateDiagramForm;
