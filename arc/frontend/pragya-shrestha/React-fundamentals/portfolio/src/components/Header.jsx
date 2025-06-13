
export default function Header() {
  return (
    <header>
      <div className="menu-icon">
        <i className="fa-solid fa-bars fa-2x"></i>
      </div>

      <nav role="navigation" aria-label="Main Navigation" className="main-nav" id="main-nav">
        <ul>
          <li><a href="#"> Home </a></li>
          <li><a href="#about"> About Me </a></li>
          <li><a href="#projects"> Projects </a></li>
          <li><a href="#experience"> Experience </a></li>
          <li><a href="#contact"> Contact </a></li>
        </ul>
        <div className="download-btn">
          <a
            href="/assets/cv.pdf"
            target="_blank"
            rel="noopener noreferrer"
            download="Pragya_Shrestha_CV.pdf"
            role="button"
            aria-label="Download CV"
            id="download-cv"
          >
            Download CV
          </a>
        </div>
      </nav>
    </header>
  );
}
