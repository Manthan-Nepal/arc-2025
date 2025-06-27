import React from 'react'
import './skills.css'
export default function Skills() {
  return (
   <>
   <section id="skills">
            <h2>My Skills</h2>
            <div className="skills-container">
                <div className="skill">
                    <h4 className="program">HTML</h4>
                    <div className="progress-bar" value="80%">
                        <div className="progress-line" style={{maxWidth:"80%"}}></div>
                    </div>
                </div>
                <div className="skill">
                    <h4 className="program">CSS</h4>
                    <div className="progress-bar" value="70%">
                        <div className="progress-line" style={{maxWidth:"70%"}}></div>
                    </div>
                </div>
                <div className="skill">
                    <h4 className="program">JavaScript</h4>
                    <div className="progress-bar" value="45%">
                        <div className="progress-line" style={{maxWidth:"45%"}}></div>
                    </div>
                </div>
                <div className="skill">
                    <h4 className="program">React</h4>
                    <div className="progress-bar" value="50%">
                        <div className="progress-line" style={{maxWidth:"50%"}}></div>
                    </div>
                </div>
                <div className="skill">
                    <h4 className="program">PHP</h4>
                    <div className="progress-bar" value="40%">
                        <div className="progress-line" style={{maxWidth:"40%"}}></div>
                    </div>
                </div>
                <div className="skill">
                    <h4 className="program">C/C++</h4>
                    <div className="progress-bar" value="35%">
                        <div className="progress-line" style={{maxWidth:"35%"}}></div>
                    </div>
                </div>
                <div className="skill">
                    <h4 className="program">Software Designing</h4>
                    <div className="progress-bar" value="60%">
                        <div className="progress-line" style={{maxWidth:"60%"}}></div>
                    </div>
                </div>
            </div>
        </section>
   </>
  )
}
