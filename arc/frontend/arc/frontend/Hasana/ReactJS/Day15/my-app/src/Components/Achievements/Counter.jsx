import { useInView, animate } from "motion/react";
import { useEffect, useRef, useState } from "react"

const Counter = ({ from, to, text }) => {
  const [count, setCount] = useState(from);
  const ref = useRef();
  const isinView = useInView(ref);

  useEffect(() => {
    const animation = animate(from, to, {
      duration: 1,
      ease: "easeOut",
      onUpdate: (prev) => {
        setCount(Math.floor(prev));
      }
    });
    return () => animation.cancel()
  }, [isinView, from, to]);

  return (
    <div className="counter" ref={ref}>
      <h1>{count}+</h1>
      <p>{text}</p>
    </div>
  )
}

export default Counter