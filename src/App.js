import React from 'react'
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Login from './pages/Login';
import Home from './pages/Home';
import Contact from './pages/Contact';
import About from './pages/About';
function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Login />} />  
      <Route path="/Home" element={<Home />} />
      <Route path="/Contact" element={<Contact />} />    
      <Route path="/About" element={<About />} />
    </Routes>
    </BrowserRouter>

  );
}

export default App;
