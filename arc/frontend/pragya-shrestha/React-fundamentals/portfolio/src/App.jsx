import About from './components/About';
import Contact from './components/Contact';
import Experience from './components/Experience';
import Footer from './components/Footer';
import Header from './components/Header';
import Hero from './components/Hero';
import Projects from './components/Projects';



function App() {
  return(
    <>
    <Header/>
    <Hero/>
      <About />
      <Projects />
      <Experience />
      <Contact />
      <Footer />
    </>
  )
}

export default App
