import { useState } from "react";
import axios from "axios";
import styled from "styled-components";

// Styled Components
const FormContainer = styled.div`
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
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
`;

const FormWrapper = styled.div`
  position: relative;
  z-index: 2;
  background-color: #1a1a1a;
  padding: 3rem;
  border-radius: 12px;
  width: 40%;
  min-width: 450px;
  max-width: 600px;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);

  @media (max-width: 1024px) {
    width: 50%;
  }

  @media (max-width: 768px) {
    width: 80%;
    min-width: unset;
    padding: 2rem;
  }
`;

const Input = styled.input`
  width: 100%;
  padding: 14px;
  font-size: 1.1rem;
  border-radius: 6px;
  border: 1px solid #555;
  background: #333;
  color: white;
  margin-bottom: 15px;
  transition: all 0.3s ease-in-out;

  &:focus {
    outline: none;
    border-color: rgb(247, 178, 66);
    box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
  }
`;

const SubmitButton = styled.button`
  background-color: #e63946;
  color: white;
  padding: 16px;
  width: 100%;
  font-size: 1.3rem;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;

  &:hover {
    background-color: #a4161a;
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(230, 57, 70, 0.3);
  }

  &:disabled {
    background-color: #555;
    cursor: not-allowed;
  }
`;

const ErrorMessage = styled.p`
  color: red;
  font-size: 1rem;
  margin-top: 10px;
`;

const DonationForm = () => {
  const [donor, setDonor] = useState("");
  const [donorEmail, setDonorEmail] = useState("");
  const [location, setLocation] = useState("");
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErrorMsg("");

    const formData = new FormData();
    formData.append("donor_id", donor);
    formData.append("donor_email", donorEmail);
    formData.append("pickup_location", location);
    formData.append("file", image);

    try {
      const response = await axios.post("http://localhost:8000/donations/create", formData);
      alert("Donation submitted successfully!");
      console.log("Response:", response.data);
    } catch (error) {
      console.error("Error:", error.response?.data || error.message);
      setErrorMsg(error.response?.data?.detail || "Failed to submit donation!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <FormContainer>
      <FormWrapper>
        <h2 style={{ color: "white", fontSize: "2rem", marginBottom: "15px" }}>
          Donate Food
        </h2>
        <form onSubmit={handleSubmit}>
          <Input type="text" placeholder="Your Name" onChange={(e) => setDonor(e.target.value)} required />
          <Input type="email" placeholder="Your Email" onChange={(e) => setDonorEmail(e.target.value)} required />
          <Input type="text" placeholder="Pickup Location" onChange={(e) => setLocation(e.target.value)} required />
          <Input type="file" accept="image/*" onChange={(e) => setImage(e.target.files[0])} required />
          {errorMsg && <ErrorMessage>{errorMsg}</ErrorMessage>}
          <SubmitButton type="submit" disabled={loading}>
            {loading ? "Submitting..." : "Submit"}
          </SubmitButton>
        </form>
      </FormWrapper>
    </FormContainer>
  );
};

export default DonationForm;
