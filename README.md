# 📘 Sudoku Solver (Python)

A lightweight, terminal-based Sudoku solver written in pure Python — no external libraries, no dependencies. Just run it and solve.

---

## ✨ Features

- 🧠 **Backtracking Algorithm** — Efficient recursive solver that handles any valid Sudoku puzzle.
- 🖊️ **Two Input Modes**:
  - **Row Mode**: Enter each row as a 9-digit string (use `0` for empty cells).
  - **Cell Mode**: Enter values one by one using a 3-digit address format (`RCV`) — e.g., `123` means *row 1, column 2, value 3*.
- ✅ **Input Validation** — Ensures all entries are within valid ranges and properly formatted.
- 🧩 **Clean Output** — Prints the solved board as a 9×9 grid.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x (no third-party packages required)

### Installation
```bash
git clone https://github.com/<your-username>/sudoku-solver.git
cd sudoku-solver
```

### Run
```bash
python sudoku_Solver.py
```

---

## 🎮 Usage

When you run the program, you'll be asked to choose an input method:

```
Choose one of the following methods to enter Sudoku numbers.
1- Enter each row as a single 9-digit line (use 0 for empty cells).
2- Enter numbers with address (e.g., 123 = row 1, col 2, value 3).
>>> 
```

### Method 1 — Row Input
Enter each row as a 9-digit string. Use `0` for empty cells.

```
Line 1: 530070000
Line 2: 600195000
Line 3: 098000060
...
```

### Method 2 — Address Input
Enter each value as `RCV` (Row, Column, Value), all digits 1–9.  
Type `end` when finished.

```
>>> 123     # row 1, col 2 → 3
>>> 519     # row 5, col 1 → 9
>>> end
```

---

## 🧠 How It Works

The solver uses a classic **backtracking** approach:

1. Find the first empty cell (`0`).
2. Try digits `1–9` in that cell.
3. For each digit, check if it's valid in the row, column, and 3×3 sub-grid.
4. Recurse. If the puzzle becomes unsolvable, backtrack and try the next digit.
5. If no empty cells remain — the puzzle is solved. 🎉

### Key Functions

| Function | Description |
|----------|-------------|
| `inputSudoku()` | Handles user input via one of the two modes. |
| `isValid(row, col, num)` | Checks whether `num` can legally be placed at `(row, col)`. |
| `solved()` | Recursive backtracking solver. Returns `True` if solved. |

---

## 📂 Project Structure

```
sudoku-solver/
│
├── sudoku_Solver.py      # Main program (single-file)
└── README.md      # You're reading it
```

---

## 🖼️ Example

**Input (Row Mode):**
```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

**Output:**
```
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]
```

---

## 🛠️ Possible Improvements

- [ ] Pretty-print the board with grid lines (`┌───┬───┬───┐`).
- [ ] Add difficulty validation (multiple solutions detection).
- [ ] Load puzzles from a file (`.txt` / `.csv`).
- [ ] GUI version with Tkinter or a web front-end.
- [ ] Unit tests with `pytest`.

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## ⭐ Show Your Support

If this project helped you, consider giving it a ⭐ on GitHub — it means a lot!

---

<p align="center">
  Made with ❤️ and Python
</p>
