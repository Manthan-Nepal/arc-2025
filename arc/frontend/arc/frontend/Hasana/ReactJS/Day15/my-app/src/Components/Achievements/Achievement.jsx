import Counter from "./Counter"
import './Achievement.css'

const experiences = [
    {
        id: 1,
        img: "/service1.png",
        title: "Personal Projects",
        counter: 13,
    },
    {
        id: 2,
        img: "/service2.png",
        title: "Graphics Designs",
        counter: 20,
    },
    {
        id: 3,
        img: "/service3.png",
        title: "Hackathons",
        counter: 4,
    },
]


const Achievements = () => {
    return (
        <div className="experiences">
            <div className="eSection">
                <h1 className="eTitle">My Experiences!</h1>
                <div className="experiencesList">
                    {experiences.map((experience) => {
                        return (

                            <div className="experience" key={experience.id}>

                                <div className="experienceIcon">
                                    <img src={experience.img} alt="" />

                                </div>
                                <div className="experienceInfo">
                                    <h2>{experience.title}</h2>
                                    <h3>{experience.counter}</h3>
                                </div>
                            </div>
                        )
                    })}
                </div>
                <div className="counterList">
                    <Counter from={0} to={5} text="Bagged Wins "></Counter>
                    <Counter from={0} to={10} text="Group Projects"></Counter>
                </div>
            </div>
        </div>
    )
}

export default Achievements;