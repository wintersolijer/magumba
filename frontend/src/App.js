// src/App.js

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Importiere die Komponenten
import Login from './components/Login';
import Register from './components/Register';

function App() {
  return (
    <Router>
      <Routes>
        {/* Login-Seite */}
        <Route path="/" element={<Login />} />

        {/* Registrierungsseite */}
        <Route path="/register" element={<Register />} />

        {/* Weitere Routen können hier hinzugefügt werden */}
      </Routes>
    </Router>
  );
}

export default App;
