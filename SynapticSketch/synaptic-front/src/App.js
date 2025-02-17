import React from 'react';
import DiagramCanvas from './components/DiagramCanvas'; // adjust path if needed
import CreateDiagramForm from './components/CreateDiagramForm';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
function App() {
  return (
    <div className="App">
      <CreateDiagramForm />
      {/* <DiagramCanvas /> */}
      <Router>
        <Routes>
          <Route path="/diagrams/:id" element={<DiagramCanvas />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
