import { FaShoppingCart } from "react-icons/fa";
import { RiArrowDropDownLine } from "react-icons/ri";
import SearchBar from "../SearchBar/SearchBar";
import "./Header.scss";

export default function Header({ filterState, setFilterState }) {
  return (
    <header className="header">
      <nav className="header__nav">
        <div className="header__menu">
          <h1 className="header__menu--title">Brands</h1>
          <RiArrowDropDownLine className="header__menu--icon" />
        </div>
        <div className="header__menu">
          <h1 className="header__menu--title">Categories</h1>
          <RiArrowDropDownLine className="header__menu--icon" />
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
