// src/Navbar.js
import React, { useState } from 'react';
import '../index.css'; // Import the CSS file for styling
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="navbar">
      <Link to ="/Home"><p className="nav-logo">MyApp</p></Link>
      <div className={`nav-items ${isOpen ? 'open' : ''}`}>
        <Link to ="/About"><a href="#about">About</a></Link>
        <Link to ="/Contact"><a href="#contact">Contact</a></Link>
      </div>
      <div className="nav-toggle" onClick={toggleMenu}>
        <div className="bar"></div>
        <div className="bar"></div>
        <div className="bar"></div>
      </div>
    </nav>
  );
};

export default Navbar;
