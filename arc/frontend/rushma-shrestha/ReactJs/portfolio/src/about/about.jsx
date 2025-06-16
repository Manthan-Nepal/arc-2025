import React from 'react'
import './about.css';
export default function About() {
  return (
    <>
    <section id="about">
            <h2>About me</h2>
            <div className="me-container">
                <div className="me">
                    <p>Name:</p>
                    <p>Rushma Shrestha</p>
                </div>
                <div className="me">
                    <p>Address:</p>
                    <p>Bhaktapur</p>
                </div>
                <div className="me">
                    <p>Age:</p>
                    <p>22 years</p>
                </div>
                <div className="me">
                    <p>Download CV</p>
                    <p><i className="fa-regular fa-file"></i></p>
                </div>
            </div>
            <div className="edu">
                <h3>Education</h3>
                <table border="1">
                    <tr>
                        <th>Year</th>
                        <th>Level</th>
                        <th>Institution</th>
                    </tr>
                    <tr>
                        <td>2019-2020/21</td>
                        <td>Plus Two</td>
                        <td>Khwopa Higher Secondary School</td>
                    </tr>
                    <tr>
                        <td>2022-2025/26</td>
                        <td>B.SC Computer Science and Information Technology</td>
                        <td>Samriddhi College</td>
                    </tr>
                </table>
            </div>

        </section>
    </>
  )
}
