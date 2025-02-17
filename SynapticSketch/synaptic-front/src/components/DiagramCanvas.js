import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';  // to read the URL param
import axios from 'axios';
import { Stage, Layer, Rect } from 'react-konva';

function DiagramCanvas() {
  const { id } = useParams(); // "id" is the dynamic part of "/diagrams/:id"
  const [shapes, setShapes] = useState([]);

  useEffect(() => {
    // Fetch the diagram data from the Django API once the component loads
    axios
      .get(`http://127.0.0.1:8000/api/diagrams/${id}/`)
      .then((response) => {
        // The diagram data might be in response.data.data.shapes
        // Adjust if your field names differ
        const { data } = response.data; // we expect "data" field in the diagram
        if (data && data.shapes) {
          setShapes(data.shapes);
        }
      })
      .catch((error) => {
        console.error('Error loading diagram:', error);
      });
  }, [id]);

  // Optional: a handler for when the user drags shapes or modifies them
  const onShapeDragEnd = (index, e) => {
    const newShapes = [...shapes];
    newShapes[index].x = e.target.x();
    newShapes[index].y = e.target.y();
    setShapes(newShapes);

    // If you want to save changes back to the server, you'd call an axios PUT here
  };

  return (
    <div>
      <h2>Diagram #{id}</h2>
      <Stage width={800} height={600} style={{ border: '1px solid #ccc' }}>
        <Layer>
          {shapes.map((shape, index) => (
            <Rect
              key={index}
              x={shape.x}
              y={shape.y}
              width={shape.width}
              height={shape.height}
              fill={shape.color || 'gray'}
              draggable
              onDragEnd={(e) => onShapeDragEnd(index, e)}
            />
          ))}
        </Layer>
      </Stage>
    </div>
  );
}

export default DiagramCanvas;
