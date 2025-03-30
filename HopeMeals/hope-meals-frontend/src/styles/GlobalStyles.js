import { createGlobalStyle } from "styled-components";

const GlobalStyles = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
  }

  body {
    background-color: #121212;
    color: white;
    line-height: 1.6;
    scroll-behavior: smooth;
    padding: 20px;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }

  section {
    padding: 40px 20px;
  }

  a {
    text-decoration: none;
    color: #4db5ff;
    transition: color 0.3s ease-in-out;
  }

  a:hover {
    color: #8ecaff;
  }

  button {
    cursor: pointer;
    padding: 12px 20px;
    border: none;
    border-radius: 8px;
    background: #4db5ff;
    color: white;
    font-size: 16px;
    font-weight: bold;
    transition: background 0.3s ease-in-out;
  }

  button:hover {
    background: #3a9de5;
  }

  /* Responsive Design */
  @media (max-width: 768px) {
    body {
      font-size: 14px;
      padding: 10px;
    }

    .container {
      padding: 15px;
    }

    section {
      padding: 30px 15px;
    }
  }
`;

export default GlobalStyles;
