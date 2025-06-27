import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./ProductDetails.scss";
export default function ProductDetails() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`https://fakestoreapi.com/products/${id}`)
      .then((res) => res.json())
      .then(setProduct)
      .catch(console.error);
  }, [id]);

  if (!product) return <p>Loading...</p>;

  return (
    <div className="productDetails">
      <img src={product.image} alt={product.title} />
      <div className="details">
        <h1>{product.title}</h1>
        <p className="desc">{product.description}</p>
        <div className="tag">
          <p>
            <strong>Price:</strong> ${product.price}
          </p>
          <p>
            <strong>Rating:</strong> {product.rating?.rate}
          </p>
        </div>
      </div>
    </div>
  );
}
