# Google Docs Grid Parser 🧩

This Python script fetches a published Google Docs page containing a table of `(x, char, y)` values, and renders them on a 2D ASCII grid.

---

## 📌 Features

- Fetches HTML content from a public **"Published to Web"** Google Docs link.
- Extracts character placement data from an HTML `<table>`.
- Renders a 2D grid of characters using their `(x, y)` coordinates.
- Simple and easy to extend.

---

## 🧾 Table Format

The Google Docs table should have **exactly 3 columns** per row:
| X | Character | Y |
|---|-----------|---|
| 5 | @         | 2 |
| 6 | #         | 2 |
| 5 | X         | 3 |

- `X`: Column index (0-based)
- `Y`: Row index (0-based)
- `Character`: The symbol to place

---
