import React from 'react'
import'./footer.css';
export default function Footer() {
  return (
        <><footer id="contact">
          <div className="contact-left">
              <p>
                  <i className="fa-brands fa-linkedin"></i>:{" "}
                  <a href="https://www.linkedin.com/in/rushma-shrestha-b58a50241/">
                      Rushma Shrestha
                  </a>
              </p>
              <p>
                  <i className="fa-brands fa-github"></i>:{" "}
                  <a href="https://github.com/rusma07">@rusma07</a>
              </p>
              <p>
                  <i className="fa-regular fa-envelope"></i>:{" "}
                  <a href="mailto:shrestharusu5@gmail.com">shrestharusu5@gmail.com</a>
              </p>
          </div>

          <div className="contact-right">
              <form className="form" action="">
                  <input className="form__input form__input--disabled" type="text" aria-labelledby="username" placeholder="Your Full Name" /><br />

                  <input type="email" aria-labelledby="email" placeholder="Email" /><br />

                  <textarea placeholder="Feedback / Message"></textarea><br />

                  <button type="submit">Submit</button>
              </form>
          </div>
      </footer><p class="credit"><em>&copy; Rushma Shrestha 2025</em> </p></>

  )
}
