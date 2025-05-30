# 📏 CSS Units Overview

CSS units are used to specify **lengths** like width, height, padding, margin, font-size, etc. They fall into **two categories**:

## Absolute Units

These are **fixed** and don’t change depending on screen or context. Useful for print styles or when you need exact control.

| Unit | Description                 | Approx Value         |
| ---- | --------------------------- | -------------------- |
| `px` | Pixels (most commonly used) | 1px = 1 dot= 1/96 in |
| `pt` | Points (used in print)      | 1pt = 1/72 in        |
| `pc` | Picas (1pc = 12pt)          |                      |
| `in` | Inches                      | 1in = 2.54cm         |
| `cm` | Centimeters                 |                      |
| `mm` | Millimeters                 |                      |

---

## Relative Units

Relative units **scale based on something else** (like font size or viewport).

| Unit  | Relative To (Font-Size) | Relative To (Spacing/Layout)     |
| ----- | ----------------------- | -------------------------------- |
| `em`  | Parent font-size        | Element's own computed font-size |
| `rem` | Root (`html`) font-size | Root (`html`) font-size          |
| `%`   | Parent font-size        | Parent element's dimensions      |

### _==Examples==_

```css
html {
  font-size: 16px;
}

h1 {
  font-size: 2rem; /* Always 32px (2 × 16px) */
  padding: 1rem; /* Always 16px */
}
```

> **Best Practice**: Use `rem` for consistent scaling across components.

### Viewport-relative units

| Unit   | Based on                           |
| ------ | ---------------------------------- |
| `vw`   | 1% of the viewport **width**       |
| `vh`   | 1% of the viewport **height**      |
| `vmin` | 1% of the **smaller** of `vw`/`vh` |
| `vmax` | 1% of the **larger** of `vw`/`vh`  |
| `90vw` | 90% of the viewport **width**      |

---

## Notes

| Use Case                 | Preferred Unit |
| ------------------------ | -------------- |
| Font sizes               | `rem`, `em`    |
| Spacing (padding/margin) | `rem`, `%`     |
| Layout widths            | `%`, `vw`      |
| Fullscreen sections      | `vh`           |
| Precise control (print)  | `px`, `pt`     |

- Use `rem` instead of `em` to avoid compounding issues in nested elements.
- Use `vw` and `vh` for responsive typography or full-page sections.
- Default browser font-size is usually `16px` = `1rem`.

---

## 🧩 Responsive Grid with `auto-fill` and `auto-fit`

Both `auto-fill` and `auto-fit` are used in combination with `repeat()` and `minmax()` to create responsive layouts that automatically adjust the number of columns based on the container size.

### Key Concepts

| Property             | Description                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| `auto-fill`          | Fills the row with as many columns as possible, even if some are empty placeholders.           |
| `auto-fit`           | Same as `auto-fill`, but it collapses empty columns, so grid items stretch to fill the space.  |
| `minmax(285px, 1fr)` | Each column should be at least 285px wide, and can grow to take 1 fraction of remaining space. |
| `gap: 2rem`          | Adds **2rem gap** between **columns and rows** (horizontally and vertically).                  |

---

## Example

1.  ==**Auto-fill**==

```css
.grid-auto-fill {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(285px, 1fr));
  gap: 2rem;
}
```

![[Pasted image 20250530102722.png]]

2. ==**Auto-fit**==

```css
.grid-auto-fit {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(285px, 1fr));
  gap: 2rem;
}
```

![[Pasted image 20250530103312.png]]

## Why You See Vertical Gaps in `auto-fit`

When the viewport width cannot accommodate another 285px-wide column **plus** the 2rem gap, the grid breaks to the next row, this creates **vertical spacing**.

- This gap isn't a "visual bug", it's from `gap: 2rem` and normal **grid row behavior**.

---

## Visual Summary

| Property    | Behavior                                        |
| ----------- | ----------------------------------------------- |
| `auto-fill` | Creates empty column tracks if not enough items |
| `auto-fit`  | Stretches items by collapsing empty columns,    |

---
