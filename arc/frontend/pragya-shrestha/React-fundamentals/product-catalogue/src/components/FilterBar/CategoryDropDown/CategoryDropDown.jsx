import useProducts from "../../../hooks/products";
import "./CategoryDropDown.scss";
export default function CategoryDropDown({ setFilterState }) {
  const [products] = useProducts();

  const categories = [...new Set(products.map((product) => product.category))];

  const handleCategoryClick = (category) => {
    setFilterState((prev) => ({ ...prev, category }));
  };

  return (
    <div className="category-dropdown">
      <ul>
        <li onClick={() => handleCategoryClick("")}>All Categories</li>
        {categories.map((item) => (
          <li key={item} onClick={() => handleCategoryClick(item)}>
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
}
