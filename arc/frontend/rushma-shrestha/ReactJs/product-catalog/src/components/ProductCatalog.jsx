import React, { useState } from "react";
import ProductCard from "./ProductCard";
import './product.css'

const initialProducts = [
  { id: 1, name: "iPhone 14", category: "Electronics", price: 799 },
  { id: 2, name: "Denim Jacket", category: "Clothing", price: 49 },
  { id: 3, name: "Electric Kettle", category: "Home Appliances", price: 29 },
  { id: 4, name: "AirPods Pro", category: "Electronics", price: 199 },
  { id: 5, name: "Yoga Mat", category: "Fitness", price: 20 },
  { id: 6, name: "LED Lamp", category: "Home Appliances", price: 15 },
];

export default function ProductCatalog() {
  const [searchTerm, setSearchTerm] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("All");

  const categories = ["All", ...new Set(initialProducts.map(p => p.category))];

  const filteredProducts = initialProducts.filter(product => {
    const matchesSearch = product.name.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = categoryFilter === "All" || product.category === categoryFilter;
    return matchesSearch && matchesCategory;
  });
  

  return (
    <div>
      <h1>Product Catalog</h1>

      <div className="controls">
        <input type="text" placeholder="Search product" value={searchTerm} onChange={e=>setSearchTerm(e.target.value)} />
        <select name="select-products" id="select-product" value={categoryFilter} onChange={e=> setCategoryFilter(e.target.value)}>
            {categories.map((cate,index)=>(
                <option key={index} value={cate}>{cate}</option>
            ))}
        </select>
      </div>

      <div className="product-list">
        {filteredProducts.length?(filteredProducts.map((product)=>( <ProductCard key={product.id} product={product}/>))):(<p>No products available</p>)}
      </div>
    </div>
  );
}
