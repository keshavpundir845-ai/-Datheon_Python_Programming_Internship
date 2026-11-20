import random

words = ["python", "computer", "hangman", "keyboard", "developer"]
secret_word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_attempts:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    
    if all(letter in guessed_letters for letter in secret_word):
        print(f"You Won! Word was {secret_word}")
        break
        
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("Already guessed!")
        continue
        
    guessed_letters.add(guess)
    
    if guess not in secret_word:
        wrong_guesses += 1
        print(f"Wrong! Attempts left: {max_attempts - wrong_guesses}")
else:
    print(f"Game Over! Word was {secret_word}")
