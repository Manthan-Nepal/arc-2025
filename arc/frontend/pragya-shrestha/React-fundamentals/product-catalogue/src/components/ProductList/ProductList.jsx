import useProducts from "../../hooks/products";
import ProductCard from "../ProductCard/ProductCard";
import "./ProductList.scss";

export default function ProductList({ searchTerm, sortOrder, category }) {
  const [products, setProducts] = useProducts();

  let filtered = products;
  if (searchTerm) {
    filtered = filtered.filter((product) =>
      product.title.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }

  if (category) {
    filtered = filtered.filter((product) => product.category === category);
  }

  const sortedProducts = [...filtered].sort((a, b) =>
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
