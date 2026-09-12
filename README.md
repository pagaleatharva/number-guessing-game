# 🎯 Python Number Guessing Game

A simple interactive **Number Guessing Game built with Python**. The computer randomly selects a number between 1 and 100, and the player gets a maximum of 7 attempts to guess it.

## 📌 Features

* 🎲 Random number generation from 1 to 100
* 🔢 Maximum 7 guessing attempts
* ⬆️ Gives a **"Higher!"** hint when the guess is too low
* ⬇️ Gives a **"Lower!"** hint when the guess is too high
* ✅ Displays the number of attempts when the player wins
* ❌ Handles invalid/non-numeric input
* 🔄 Allows the player to restart the game
* 👋 Displays a goodbye message when the player exits

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* Functions
* `while` loops
* `if-elif-else` conditions
* Exception handling (`try-except`)
* User input

## 📂 Project Structure

```text
python-number-guessing-game/
│
├── game.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/pagaleatharva/python-number-guessing-game.git
```

### 2. Open the project folder

```bash
cd python-number-guessing-game
```

### 3. Run the game

```bash
python game.py
```

## 🎮 How to Play

1. The computer generates a secret number between **1 and 100**.
2. Enter your guess when prompted.
3. The game gives you a hint:

   * `Higher!` → Your guess is too low.
   * `Lower!` → Your guess is too high.
4. You have a maximum of **7 valid attempts**.
5. If you guess correctly, you win.
6. After the game ends, you can choose whether to play again.

### Example

```text
Enter your guess: 50
Higher!

Enter your guess: 75
Lower!

Enter your guess: 63
Correct! You guessed it in 3 attempts.

Play again? (yes/no): no
Thanks for playing!
```

## 🧠 What I Learned

This project helped me practice:

* Writing and calling Python functions
* Using loops to control program flow
* Using conditional statements
* Handling invalid user input with `try-except`
* Using Python's `random` module
* Understanding `break` and `continue`
* Creating a replayable program
* Organizing a small Python project for GitHub

## 🚀 Future Improvements

Possible improvements for future versions:

* Add difficulty levels
* Add a scoring system
* Track the best score
* Add a graphical user interface
* Add multiplayer functionality
* Store game statistics

## 👨‍💻 Author

**Atharva Pagale**

GitHub: [@pagaleatharva](https://github.com/pagaleatharva)

---

⭐ If you found this project useful, feel free to star the repository!
