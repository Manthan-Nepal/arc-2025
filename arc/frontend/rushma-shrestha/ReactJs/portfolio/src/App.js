import logo from './logo.svg';
import './App.css';
import Navbar from './Navbar/nav';
import Hero from './hero/hero';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import About from './about/about'
import Skills from './skills/skills';
import Footer from './footer/footer';
import Project from './project/project';

function App() {
  return (
    <>
    <Navbar/>
    <Hero/>
    <About/>
    <Project/>
    <Skills/>
    <Footer/>
    </>

  );
}

export default App;
