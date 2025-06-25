import { FaRegStar, FaShoppingCart, FaStar, FaStarHalf } from "react-icons/fa";
import { useCart } from "../../context/CartContext.jsx";
import "./ProductCard.scss";

export default function ProductCard({ product }) {
  const { cartItems, toggleCartItem } = useCart();
  const isInCart = cartItems.some((item) => item.id === product.id);

  const rating = product.rating?.rate || 0;

  const decimal = rating - Math.floor(rating);
  let fullStars;
  let hasHalfStar = false;

  if (decimal < 0.3) {
    fullStars = Math.floor(rating);
  } else if (decimal >= 0.3 && decimal < 0.8) {
    fullStars = Math.floor(rating);
    hasHalfStar = true;
  } else {
    fullStars = Math.ceil(rating);
  }

  const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);

  const stars = [
    ...Array(fullStars).fill(<FaStar />),
    ...(hasHalfStar ? [<FaStarHalf key="half" />] : []),
    ...Array(emptyStars).fill(<FaRegStar />),
  ];

  return (
    <div className="productCard">
      <div className="productCard__image">
        <img src={product.image} alt={product.title} />
      </div>
      <h2>{product.title}</h2>
      <p className="productCard__description">{product.description}</p>

      <div className="productCard__tags">
        <p className="productCard__tags--price">$ {product.price}</p>
        <div className="productCard__tags--rate">
          <p>{rating}</p>
          <span className="productCard__tags--stars">
            {stars.map((icon, i) => (
              <span key={i}>{icon}</span>
            ))}
          </span>
        </div>

        <button
          className={`productCard__tags--cartButton ${
            isInCart ? "in-cart" : ""
          }`}
          onClick={() => toggleCartItem(product)}
        >
          <FaShoppingCart className="cart__icon" />
        </button>
      </div>
    </div>
  );
}
