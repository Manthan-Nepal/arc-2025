// import logo from './logo.svg';
import './App.css';
import Hero from './Components/Hero/Home';
import Achievements from './Components/Achievements/Achievement';

function App() {
  return (
    <div>
      <section id='hero'>
        <Hero></Hero>
      </section>
      <section id='achievements'>
        <Achievements></Achievements>
      </section>
      <section></section>
      <section></section>
    </div>
  );
}

export default App;
