import styled from "styled-components";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";

const AboutContainer = styled.div`
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 20px;
  background: url("https://c1.wallpaperflare.com/preview/350/663/606/street-beggar-homeless-poverty.jpg") no-repeat center center/cover;
  background-size: cover;
  background-position: center;
  overflow: hidden;

  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    z-index: 1;
  }
`;

const Content = styled.div`
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 15px;
  text-align: center;
`;

const Heading = styled(motion.h1)`
  font-size: 2.5rem;
  font-weight: 700;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 1px;
  line-height: 1.3;
  margin-bottom: 15px;

  @media (max-width: 768px) {
    font-size: 2rem;
  }
`;


const Step = styled(motion.p)`
  font-size: 1.3rem;
  color: #f6cdc3;
  max-width: 750px;
  font-weight: 400;
  font-family: "Poppins", sans-serif;
  line-height: 1.5;
  margin-bottom: 15px;
  text-align: center;

  @media (max-width: 768px) {
    font-size: 1.1rem;
    max-width: 90%;
  }
`;



const Button = styled(Link)`
  background: linear-gradient(135deg, #d32f2f, #b71c1c);
  padding: 14px 40px;
  border-radius: 50px;
  font-size: 1.3rem;
  color: white;
  font-weight: bold;
  text-transform: uppercase;
  transition: all 0.3s ease-in-out;
  margin-top: 15px;
  text-decoration: none;
  font-family: "Poppins", sans-serif;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
  display: inline-block;

  &:hover {
    background: linear-gradient(135deg, #b71c1c, #6a1b1a);
    transform: scale(1.08);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
  }

  @media (max-width: 768px) {
    width: 100%;
    text-align: center;
    padding: 12px;
  }
`;

const About = () => {
  return (
    <AboutContainer>
      <Content>
        <Heading
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, ease: "easeOut" }}
        >
          About Us
        </Heading>

        <Step
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.2, ease: "easeOut", delay: 0.3 }}
        >
          🌍 We are committed to ending hunger by rescuing surplus food from restaurants and delivering it to those in need. Through our initiative, we not only reduce food waste but also create a community of compassionate contributors who earn rewards for making a difference. Every meal shared is a step toward a world where no one sleeps hungry.
        </Step>
        <Step
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.4, ease: "easeOut", delay: 0.5 }}
        >
          1️⃣ Fill in the details and upload a photo of the food.
        </Step>
        <Step
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.6, ease: "easeOut", delay: 0.7 }}
        >
          2️⃣ Get matched with the nearest person in need.
        </Step>
        <Step
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.8, ease: "easeOut", delay: 0.9 }}
        >
          3️⃣ Earn points and contribute to NGOs.
        </Step>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 2, ease: "easeOut", delay: 1 }}
        >
          <Button to="/donate">Join Our Mission</Button>
        </motion.div>
      </Content>
    </AboutContainer>
  );
};

export default About;
