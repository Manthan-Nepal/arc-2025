
const ExperienceSection = () => {
  return (
    <section className="projects-section" id="experience">
      <h2 className="primary-heading">My Experiences</h2>
      <div className="experience-container">
        {[1, 2, 3, 4].map((item) => (
          <div className="experience-card" key={item}>
            <h3>Title {item}</h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deserunt
              quibusdam voluptatum veniam accusamus
            </p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ExperienceSection;
