import { useEffect, useState } from "react";
import { getLocal, setLocal } from "../../utils/LocalStorageHelper";
import ProductCard from "../ProductCard/ProductCard";
import "./ProductList.scss";

export default function ProductList({ searchTerm, sortOrder }) {
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

  const filteredProducts = products.filter((product) =>
    product.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const sortedProducts = [...filteredProducts].sort((a, b) =>
    sortOrder === "asc"
      ? a.title.localeCompare(b.title)
      : b.title.localeCompare(a.title)
  );

  return (
    <div className="product-list">
      {sortedProducts.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
