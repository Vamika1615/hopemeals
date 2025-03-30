import { useState } from "react";
import { QrReader } from "react-qr-reader";
import axios from "axios";
import styled from "styled-components";

const ScannerContainer = styled.div`
  text-align: center;
  padding: 2rem;
`;

const Message = styled.p`
  color: #ffb703;
  font-size: 1.2rem;
  margin-top: 1rem;
`;

const QRScanner = () => {
  const [result, setResult] = useState("");

  const handleScan = async (data) => {
    if (data) {
      setResult("Verifying QR Code...");
      try {
        const response = await axios.get(`http://localhost:8000/donations/verify-qr/${data}`);
        setResult(response.data.message);
      } catch (error) {
        console.log(error)
        setResult("Invalid QR Code");
      }
    }
  };

  return (
    <ScannerContainer>
      <h2>Scan QR Code to Verify Pickup</h2>
      <QrReader
        constraints={{ facingMode: "environment" }}
        onResult={(result) => handleScan(result?.text)}
        style={{ width: "300px", margin: "auto" }}
      />
      <Message>{result}</Message>
    </ScannerContainer>
  );
};

export default QRScanner;
