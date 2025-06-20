import { useState } from "react";
import { FaShoppingCart } from "react-icons/fa";
import { RiArrowDropDownLine } from "react-icons/ri";
import CategoryDropDown from "../FilterBar/CategoryDropDown/CategoryDropDown";
import SearchBar from "../SearchBar/SearchBar";
import "./Header.scss";

export default function Header({ filterState, setFilterState }) {
  const [showCategoryDropdown, setShowCategoryDropdown] = useState(false);

  const toggleDropdown = () => {
    setShowCategoryDropdown((prev) => !prev);
  };

  return (
    <header className="header">
      <nav className="header__nav">
        <div className="header__menu">
          <h1 className="header__menu--title">Brands</h1>
          <RiArrowDropDownLine className="header__menu--icon" />
        </div>

        <div className="header__menu category_menu" onClick={toggleDropdown}>
          <h1 className="header__menu--title">Categories</h1>
          <RiArrowDropDownLine
            className={`header__menu--icon ${
              showCategoryDropdown ? "rotated" : ""
            }`}
          />
          {showCategoryDropdown && (
            <CategoryDropDown
              setFilterState={setFilterState}
              closeDropdown={() => setShowCategoryDropdown(false)}
            />
          )}
        </div>

        <SearchBar filterState={filterState} setFilterState={setFilterState} />
      </nav>

      <div className="cart">
        <FaShoppingCart className="cart__icon" />
        <span className="cart__count">0</span>
      </div>
    </header>
  );
}
