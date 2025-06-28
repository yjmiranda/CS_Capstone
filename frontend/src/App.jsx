import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import LandingPage from "./components/LandingPage.jsx"
import FormPage from "./components/FormPage.jsx"
import LearnPage from "./components/LearnPage.jsx"

import './App.css'


function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<LandingPage/>} />
          <Route path="/predict" element={<FormPage/>} />
          <Route path="/learn" element={<LearnPage/>} />
        </Routes>
      </Router>
  );
}

export default App
