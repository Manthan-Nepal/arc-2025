import React from 'react';
import   './nav.css';
import { NavLink } from 'react-router-dom';

export default function Navbar() {
  return (
    <div> 
        <header>
        <div className="head">
            <h1>R.S</h1>
        </div>
        <nav>
            <a href="#hero" className="nav-link">Home</a>
            <a href="#about" className="nav-link">About me</a>
            <a href="#skills" className="nav-link">Skills</a>
            <a href="#contact" className="nav-link">Contact Me!</a>
    
        </nav>
    </header></div>
  )
}
