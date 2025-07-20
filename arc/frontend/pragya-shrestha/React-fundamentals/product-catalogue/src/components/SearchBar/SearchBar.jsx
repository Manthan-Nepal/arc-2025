import { useEffect, useState } from "react";
import { FaSortAmountDown, FaSortAmountDownAlt } from "react-icons/fa";
import { FaMagnifyingGlass } from "react-icons/fa6";
import "./SearchBar.scss";

export default function SearchBar({ filterState, setFilterState }) {
  const { searchTerm, sortOrder } = filterState;
  const [value, setValue] = useState(searchTerm || "");

  useEffect(() => {
    setValue(searchTerm);
  }, [searchTerm]);

  useEffect(() => {
    const handler = setTimeout(() => {
      setFilterState((prev) => ({ ...prev, searchTerm: value }));
    }, 500);

    return () => clearTimeout(handler);
  }, [value, setFilterState]);

  const handleChange = (e) => setValue(e.target.value);

  const handleSortChange = () => {
    setFilterState((prev) => ({
      ...prev,
      sortOrder: prev.sortOrder === "asc" ? "desc" : "asc",
    }));
  };

  return (
    <div className="searchBar">
      <button className="searchBar__searchButton">
        <FaMagnifyingGlass className="searchBar__searchButton--icon" />
      </button>

      <input
        type="text"
        className="searchBar__input"
        placeholder="Search product"
        value={value}
        onChange={handleChange}
      />

      <button className="searchBar__sortButton" onClick={handleSortChange}>
        {sortOrder === "asc" ? (
          <FaSortAmountDownAlt className="searchBar__sortButton--icon" />
        ) : (
          <FaSortAmountDown className="searchBar__sortButton--icon" />
        )}
      </button>
    </div>
  );
}
