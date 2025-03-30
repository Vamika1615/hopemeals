import styled from "styled-components";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";

const HomeContainer = styled.div`
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 20px 20px; /* Adjusted padding */
  background: url("https://c1.wallpaperflare.com/preview/350/663/606/street-beggar-homeless-poverty.jpg") 
    no-repeat center center/cover;
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
    background: rgba(0, 0, 0, 0.85);
    z-index: 1;
  }

  @media (max-width: 768px) {
    padding-top: 100px;
  }
`;

const Content = styled.div`
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  text-align: center;
`;

const HeadingWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 700px;
  width: 100%;
`;

const Heading = styled(motion.h1)`
  font-size: 3rem;
  font-weight: 700;
  font-family: "Poppins", sans-serif;
  color: #ffffff;
  text-transform: uppercase;
  letter-spacing: 1px;
  width: 100%;
  text-align: center;
  line-height: 1.3;

  @media (max-width: 768px) {
    font-size: 2rem;
  }
`;

const WhiteSubheading = styled(motion.p)`
  font-size: 1.4rem;
  color: rgb(247, 178, 66);
  max-width: 600px;
  font-weight: 500;
  font-family: "Poppins", sans-serif;
  margin-bottom: 25px;

  @media (max-width: 768px) {
    font-size: 1.2rem;
    margin-bottom: 20px;
  }
`;

const Button = styled(Link)`
  background-color: #6a1b1a;
  padding: 12px 35px;
  border-radius: 50px;
  font-size: 1.2rem;
  color: white;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  margin-top: 5px;
  text-decoration: none;
  font-family: "Poppins", sans-serif;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);

  &:hover {
    background-color: #4e1211;
    color: #ffffff;
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 12px 20px rgba(0, 0, 0, 0.5);
  }

  @media (max-width: 768px) {
    width: 100%;
    text-align: center;
    padding: 10px;
  }
`;

const Home = () => {
  return (
    <HomeContainer>
      <Content>
        <HeadingWrapper>
          <Heading
            initial={{ opacity: 0, y: 30, scale: 0.9 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 1, ease: "easeOut" }}
          >
            Every Plate Counts.
          </Heading>
          <Heading
            initial={{ opacity: 0, y: 30, scale: 0.9 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 1.2, ease: "easeOut", delay: 0.3 }}
          >
            Every Life Matters.
          </Heading>
        </HeadingWrapper>

        <WhiteSubheading
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.8, ease: "easeOut", delay: 0.8 }}
        >
          Join us in making an impact today!
        </WhiteSubheading>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 2, ease: "easeOut", delay: 1 }}
        >
          <Button to="/donate">Donate Food</Button>
        </motion.div>
      </Content>
    </HomeContainer>
  );
};

export default Home;
