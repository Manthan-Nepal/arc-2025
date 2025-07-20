import { createRoot } from "react-dom/client";
import { ToastContainer } from "react-toastify";
import App from "./App.jsx";
import { CartProvider } from "./context/CartContext.jsx";
import "./styles/main.scss";

createRoot(document.getElementById("root")).render(
  <CartProvider>
    <App />
    <ToastContainer position="top-center" autoClose={2000} />
  </CartProvider>
);
