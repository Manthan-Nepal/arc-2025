import React from 'react'
import './project.css'
export default function Project() {
  return (
    <section id="myprojects">
            <h2> My Projects</h2>
            <div class="project-container">
                <div class="project">
                    <h3>CookBook</h3>
                    <p>CookBook is a web-based application that provides the users recipes about the foods as per their
                        choices. This web allows only authenticated users to access the recipes whereas the admin are
                        able to add more recipes in the website. It is portable as well, as it is responsive with
                        mobile, tablets and desktop.</p>
                    <button>Learn More</button>
                </div>
                <div class="project">
                    <h3>PrajaMitra</h3>
                    <p>PrajaMitra is a web-based application that connects remote areas with the government portal. This
                        web allows only authenticated users to access the services of complaining grievance ,
                        citizenship download and further service of paying bills of telephone, internet etc. It is
                        portable as well, as it is responsive with mobile, tablets and desktop. </p>
                    <button>Learn More</button>
                </div>
                <div class="project">
                    <h3>SpeedTest</h3>
                    <p>SpeedTest is a web-based application that provides the users recipes about the foods as per their
                        choices. This web allows only authenticated users to access the recipes whereas the admin are
                        able to add more recipes in the website. It is portable as well, as it is responsive with
                        mobile, tablets and desktop.</p>
                    <button>Learn More</button>
                </div>
            </div>
        </section>
  )
}
