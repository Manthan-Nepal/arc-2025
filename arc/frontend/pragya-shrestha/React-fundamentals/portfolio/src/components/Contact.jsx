const ContactSection = () => {
  return (
    <section className="contact-section" id="contact">
      <div className="contact-title">
        <h2>Contact Me</h2>
        <p>
          If you have any questions or want to get in touch, feel free to reach out!
        </p>
      </div>
      <form>
        <input
          type="email"
          id="email"
          name="email"
          placeholder="Email"
          className="form-input"
          required
        />
        <textarea
          id="message"
          name="message"
          rows="3"
          placeholder="Any Messages"
          className="form-input"
          required
        ></textarea>
        <button type="submit" className="submit-btn">Submit</button>
      </form>
    </section>
  );
};

export default ContactSection;
