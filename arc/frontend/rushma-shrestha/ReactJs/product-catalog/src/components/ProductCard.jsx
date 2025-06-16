import React from 'react';

export default function ProductCard({ product }) {
  // console.log("Rendering product", product);
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p>Category: {product.category}</p>
      <p>Price: ${product.price.toFixed(2)}</p>
    </div>
    
  );
}
