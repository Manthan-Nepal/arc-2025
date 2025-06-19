import { useState } from "react";
import { FaMagnifyingGlass } from "react-icons/fa6";
// import { FaSortAmountDown } from "react-icons/fa";
import { FaSortAmountDownAlt } from "react-icons/fa";
import "./SearchBar.scss";
export default function SearchBar() {
  const [value, setValue] = useState();
  const handleChange = (e) => {
    setValue(e.target.value);
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
      <button className="searchBar__sortButton">
        <FaSortAmountDownAlt className="searchBar__sortButton--icon" />
        {/* <FaSortAmountDown className="searchBar__sortButton--icon" /> */}
      </button>
    </div>
  );
}
