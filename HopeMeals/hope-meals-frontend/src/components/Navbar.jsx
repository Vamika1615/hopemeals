import { Link } from "react-router-dom";
import styled from "styled-components";

const NavbarContainer = styled.nav`
  width: 100%;
  background: linear-gradient(135deg, #d62828, #6a1b1a);
  padding: 1.2rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 80px;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease-in-out;

  @media (max-width: 768px) {
    flex-direction: column;
    height: auto;
    padding: 1rem;
  }
`;

const Logo = styled.h2`
  color: white;
  font-size: 1.8rem;
  font-weight: bold;
  letter-spacing: 1px;
  cursor: pointer;
  transition: 0.3s;

  &:hover {
    color: #ffd700;
    transform: scale(1.1);
  }
`;

const NavLinks = styled.div`
  display: flex;
  gap: 20px;

  a {
    color: white;
    font-weight: bold;
    text-decoration: none;
    font-size: 1.2rem;
    padding: 10px 15px;
    border-radius: 5px;
    position: relative;
    overflow: hidden;
    transition: color 0.3s, transform 0.2s;

    &:hover {
      color: #ffd700;
      transform: translateY(-2px);
    }

    &::after {
      content: "";
      position: absolute;
      left: 50%;
      bottom: 0;
      width: 0;
      height: 2px;
      background: #ffd700;
      transition: all 0.3s ease-in-out;
      transform: translateX(-50%);
    }

    &:hover::after {
      width: 100%;
    }

    @media (max-width: 768px) {
      display: block;
      font-size: 1.5rem;
      text-align: center;
      padding: 10px;
    }
  }
`;

const Navbar = () => {
  return (
    <NavbarContainer>
      <Logo>🍽️ HopeMeals</Logo>
      <NavLinks>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link> {/* Updated this line */}
        <Link to="/donate">Donate</Link>
        <Link to="/verify">Verify QR</Link>
        <Link to="/dashboard">NGO Dashboard</Link>
      </NavLinks>
    </NavbarContainer>
  );
};

export default Navbar;
