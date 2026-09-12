# 🎯 Python Number Guessing Game

A simple interactive **Number Guessing Game built using Python**. The computer generates a random number between 1 and 100, and the player gets up to 7 attempts to guess the correct number.

## 📌 Features

* 🎲 Generates a random number between 1 and 100
* 🔢 Gives the player up to 7 attempts
* ⬆️ Displays **"Higher"** when the guess is too low
* ⬇️ Displays **"Lower"** when the guess is too high
* ✅ Displays **"Correct"** when the player guesses the number
* ❌ Shows the secret number when all attempts are used
* 🔄 Allows the player to play the game again

## 🛠️ Technologies Used

* Python 3
* `random` module
* Functions
* `while` loop
* `if-elif-else` conditions
* `break` and `continue`

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

### 3. Run the program

```bash
python game.py
```

## 🎮 How to Play

1. The computer randomly selects a number between **1 and 100**.
2. Enter your guess.
3. The game gives you a hint:

   * **Higher** → Your guess is smaller than the secret number.
   * **Lower** → Your guess is greater than the secret number.
4. You have a maximum of **7 attempts**.
5. If you guess correctly, the game displays **"Correct"**.
6. If you use all 7 attempts, the secret number is displayed.
7. After the game ends, you can choose whether to play again.

## 💻 Example

```text
enter the no 50
higher

enter the no 75
lower

enter the no 63
correct

play again(yes/no): no
```

## 🧠 Concepts Practiced

This project helped me practice:

* Creating and calling functi
