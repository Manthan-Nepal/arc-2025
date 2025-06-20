import { useEffect, useState } from "react";
import Header from "./components/Header/Header";
import ProductList from "./components/ProductList/ProductList";
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
    <>
      <Header filterState={filterState} setFilterState={setFilterState} />
      <ProductList
        searchTerm={filterState.searchTerm}
        sortOrder={filterState.sortOrder}
        category={filterState.category}
      />
    </>
  );
}

export default App;
