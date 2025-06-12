import "./home.css";
import { motion } from "framer-motion";

const awardVariants = {
  initial: {
    x: -100,
    opacity: 0,
  },
  animate: {
    x: 0,
    opacity: 1,
    transition: {
      duration: 1,
      staggerChildren: 0.2,
    },
  },
};

const followVariants = {
  initial: {
    y: -100,
    opacity: 0,
  },
  animate: {
    y: 0,
    opacity: 1,
    transition: {
      repeat: Infinity,
      repeatDelay: 2,
      duration: 2,
      staggerChildren: 0.2,
    },
  },
};

const Hero = () => {
  return (
    <div className="home">
      <div className="hsection left">
        <motion.h1
          initial={{ y: -100, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 1 }}
          className="hTitle"
        >
          Hello There, <br />
          <span>I&apos;m Hasana!</span>
        </motion.h1>

        <motion.div
          variants={awardVariants}
          initial="initial"
          animate="animate"
          className="awards"
        >
          <motion.h2 variants={awardVariants}>Open To Work</motion.h2>
          <motion.p variants={awardVariants}>
            Curious Computer Engineering student building impactful tech solutions.
          </motion.p>

          <motion.div className="awardList" variants={awardVariants}>
            <a href="https://github.com/hasana0123">
              <motion.img variants={awardVariants} src="/github.png" alt="" />
            </a>
            <a
              href="https://mail.google.com/mail/?view=cm&to=manandharhasana07@gmail.com"
              target="_blank"
            >
              <motion.img variants={awardVariants} src="/gmail.jpg" alt="" />
            </a>
            <a href="https://www.linkedin.com/in/hasana-manandhar-129301261/">
              <motion.img variants={awardVariants} src="/linkedin.png" alt="" />
            </a>
          </motion.div>
        </motion.div>

        <motion.a
          animate={{ y: [0, 5], opacity: [0, 1, 0] }}
          transition={{
            repeat: Infinity,
            duration: 4,
            ease: "easeInOut",
          }}
          href="#achievements"
          className="scroll"
        >
          <svg
            width="50px"
            height="50px"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M5 9C5 5.134 8.134 2 12 2C15.866 2 19 5.134 19 9V15C19 18.866 15.866 22 12 22C8.134 22 5 18.866 5 15V9Z"
              stroke="white"
              strokeWidth="1"
            />
            <motion.path
              animate={{ y: [0, 3] }}
              transition={{
                repeat: Infinity,
                duration: 4,
                ease: "easeInOut",
              }}
              d="M12 5V8"
              stroke="white"
              strokeWidth="1"
              strokeLinecap="round"
            />
          </svg>
        </motion.a>
      </div>

      <div className="hsection right">
        <motion.div
          variants={followVariants}
          initial="initial"
          animate="animate"
          className="follow"
        >
          <motion.a
            variants={followVariants}
            href="https://www.instagram.com/smooth.like.buttero.o?igsh=ZnNuMncwM2Z0dHNw"
          >
            <img src="/instagram.png" alt="" />
          </motion.a>
          <motion.a variants={followVariants} href="/">
            <img src="/facebook.png" alt="" />
          </motion.a>
          <motion.a variants={followVariants} href="https://x.com/lifeneedsch33s3">
            <img src="/x.png" alt="" />
          </motion.a>
          <motion.div variants={followVariants} className="followTextainer">
            <div className="followText">FOLLOW ME</div>
          </motion.div>
        </motion.div>

        <motion.div
          animate={{ opacity: [0, 1] }}
          transition={{ duration: 1 }}
          className="certificate"
        >
          <div className="images">
            <img src="/khwopa.png" alt="" />
            <img src="/ioe.png" alt="" />
          </div>
          FINAL YEAR STUDENT OF <br />
          BACHELORS IN <br />
          COMPUTER ENGINEERING
        </motion.div>

        <motion.a
          animate={{ x: [200, 0], opacity: [0, 1] }}
          transition={{ duration: 2 }}
          href="#contacts"
          className="contactLink"
        >
          <motion.div
            animate={{ rotate: [0, 360] }}
            transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
            className="contactButton"
          >
            <svg viewBox="0 0 200 200" width="120" height="120">
              <circle cx="100" cy="100" r="100" fill="pink" />
              <path
                id="innerCirclePath"
                fill="none"
                d="M 100,100 m -60,0 a 60,60 0 1,1 120,0 a 60,60 0 1,1 -120,0"
              ></path>
              <text className="circleText">
                <textPath href="#innerCirclePath">Hire Now •</textPath>
                <textPath href="#innerCirclePath" startOffset="45%">
                  Contact Me •
                </textPath>
              </text>
            </svg>

            <div className="arrow">
              <svg
                width="50"
                height="90"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                style={{ transform: "rotate(-45deg)" }}
              >
                <path
                  d="M5 12h14M12 5l7 7-7 7"
                  stroke="black"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </div>
          </motion.div>
        </motion.a>
      </div>

      <div className="bg">
        <div className="homeimg">
          <img src="/hasana.png" alt="" />
        </div>
      </div>
    </div>
  );
};

export default Hero;
