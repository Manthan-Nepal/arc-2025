import { useEffect, useState } from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Header from "./components/Header/Header";
import ProductList from "./components/ProductList/ProductList";
import ProductDetails from "./pages/Detail Page/ProductDetails";
import { getLocal, setLocal } from "./utils/LocalStorageHelper";

function App() {
  const [filterState, setFilterState] = useState(() => ({
    searchTerm: getLocal("searchTerm", ""),
    sortOrder: getLocal("sortOrder", "asc"),
    category: getLocal("category", ""),
  }));

  useEffect(() => {
    setLocal("searchTerm", filterState.searchTerm);
    setLocal("sortOrder", filterState.sortOrder);
    setLocal("category", filterState.category);
  }, [filterState]);

  return (
    <Router>
      <Header filterState={filterState} setFilterState={setFilterState} />
      <Routes>
        <Route
          path="/"
          element={
            <ProductList
              searchTerm={filterState.searchTerm}
              sortOrder={filterState.sortOrder}
              category={filterState.category}
            />
          }
        />
        <Route path="/product/:id" element={<ProductDetails />} />
      </Routes>
    </Router>
  );
}

export default App;
