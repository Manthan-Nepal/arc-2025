import React from 'react'
import "./hero.css"
import rushma from"./images/rushma.png";
export default function Hero() {
  return (
    <div>
        <section id="hero">
            <div className="hero-left">
                <h1>HI!</h1>
                <h3>I am <span style={{color:"rgb(172, 190, 137)",fontFamily:"Dancing script,cursive"}}>Rushma
                        Shrestha</span>
                </h3>
                <p>Front-End Developer</p>
                <h2>Welcome to my portfolio!</h2>
                <aside>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                    labore
                    et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                    aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                    cillum
                    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
                    officia deserunt mollit anim id est laborum.</aside>
                <button className="hero-btn1">Hire Me!</button>
                <button className="hero-btn2">My Works</button> <br/>

            </div>
            <div className="hero-right">
                <img src={rushma} alt="rushma" />
            </div>
        </section>
    </div>
  )
}
