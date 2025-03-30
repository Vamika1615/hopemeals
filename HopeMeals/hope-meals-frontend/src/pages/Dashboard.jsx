import styled from "styled-components";
import { motion } from "framer-motion";

const DashboardContainer = styled.div`
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 20px 20px;
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

const ContentWrapper = styled.div`
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
`;

const Heading = styled(motion.h1)`
  font-size: 3rem;
  font-weight: 700;
  color: #f8f9fa;
  text-transform: uppercase;
  letter-spacing: 1px;
  text-align: center;
  line-height: 1.3;

  @media (max-width: 768px) {
    font-size: 2rem;
  }
`;

const NGOList = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  padding: 20px;
`;

const NGOCard = styled(motion.div)`
  background: rgba(60, 60, 60, 0.9);
  padding: 1.5rem;
  border-radius: 12px;
  width: 280px;
  color: #f8f9fa;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease-in-out, background 0.3s ease-in-out;
  text-align: left;

  &:hover {
    transform: translateY(-5px) scale(1.05);
    background: rgba(90, 90, 90, 1);
  }

  h2 {
    margin-bottom: 0.5rem;
    font-size: 1.5rem;
    color:rgb(255, 170, 0);
  }

  p {
    font-size: 1rem;
    margin: 0.2rem 0;
    color:rgb(255, 170, 0);
  }
`;

const Dashboard = () => {
  return (
    <DashboardContainer>
      <ContentWrapper>
        <Heading
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          NGO Dashboard
        </Heading>

        <NGOList>
          <NGOCard
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.2, delay: 0.3 }}
          >
            <h2>NGO 1</h2>
            <p>Location: Mumbai</p>
            <p>Status: Active</p>
          </NGOCard>
          <NGOCard
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.2, delay: 0.5 }}
          >
            <h2>NGO 2</h2>
            <p>Location: Delhi</p>
            <p>Status: Active</p>
          </NGOCard>
          <NGOCard
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.2, delay: 0.7 }}
          >
            <h2>NGO 3</h2>
            <p>Location: Bangalore</p>
            <p>Status: Pending</p>
          </NGOCard>
        </NGOList>
      </ContentWrapper>
    </DashboardContainer>
  );
};

export default Dashboard;
