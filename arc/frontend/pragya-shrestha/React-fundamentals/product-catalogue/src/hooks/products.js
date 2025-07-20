import { useEffect, useState } from "react";
import { getLocal, setLocal } from "../utils/LocalStorageHelper.js";

export default function useProducts() {
  const [products, setProducts] = useState(() => getLocal("products", []));

  useEffect(() => {
    if (products.length === 0) {
      fetch("https://fakestoreapi.com/products")
        .then((res) => res.json())
        .then((data) => {
          setProducts(data);
          setLocal("products", data);
        })
        .catch((err) => console.error("Error fetching products:", err));
    }
  }, [products.length]);
  return [products, setProducts];
}
