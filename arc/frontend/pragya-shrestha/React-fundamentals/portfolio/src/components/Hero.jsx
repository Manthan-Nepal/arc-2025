
export default function Hero() {
  return (
    <section className="hero-section">
      <div className="hero-content">
        <div className="intro-text">
          <p>Hi, I am</p>
          <h2><span>Pragya Shrestha</span>Computer Engineer</h2>
        </div>
        <p id="description">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas distinctio nobis enim nihil aperiam ullam repellat vitae asperiores ducimus. Earum!
        </p>
        <a href="mailto:shresthapragya961@gmail.com" role="button" aria-label="Hire Pragya">
          Hire Me
        </a>
      </div>
      <div className="hero-right">
        <div className="hero-image">
          <img src="/assets/profile.jpg" alt="profile picture" />
        </div>
        <div className="hero-social">
          <a href="https://github.com/pragya-02" target="_blank" aria-label="GitHub Profile" className="social-icon" rel="noopener noreferrer">
            <i className="fa-brands fa-github"></i>
          </a>
          <a href="https://www.linkedin.com/in/pragya-shrestha-cs/" aria-label="LinkedIn Profile" target="_blank" rel="noopener noreferrer" className="social-icon">
            <i className="fa-brands fa-linkedin-in"></i>
          </a>
          <a href="https://www.facebook.com/share/16XyhVcad5/" target="_blank" rel="noopener noreferrer" aria-label="Facebook Profile" className="social-icon">
            <i className="fa-brands fa-facebook"></i>
          </a>
        </div>
      </div>
    </section>
  );
}
