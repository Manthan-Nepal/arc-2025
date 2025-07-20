const ProjectsSection = () => {
  return (
    <section className="projects-section" id="projects">
      <h2 className="primary-heading">My Projects</h2>
      <div className="projects-container">
        {[1, 2, 3].map((item) => (
          <div className="project-card" key={item}>
            <img src="/assets/project.png" alt={`Project ${item}`} />
            <h3>Project Title {item}</h3>
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deserunt
              quibusdam voluptatum veniam accusamus
            </p>
            <a href="#" className="project-link">View Project</a>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ProjectsSection;
