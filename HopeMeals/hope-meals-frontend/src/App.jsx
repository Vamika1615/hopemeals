import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import GlobalStyles from "./styles/GlobalStyles";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import DonationForm from "./components/DonationForm";
import QRScanner from "./components/QRScanner";
import Dashboard from "./pages/Dashboard";
import AboutPage from "./pages/AboutPage"; // ✅ Import AboutPage

function App() {
  return (
    <Router>
      <GlobalStyles />
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<AboutPage />} /> {/* ✅ Add About Route */}
        <Route path="/donate" element={<DonationForm />} />
        <Route path="/verify" element={<QRScanner />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
