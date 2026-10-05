import random

def play_hangman():
    # 1. Use a small list of 5 predefined words
    word_list = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
    word = random.choice(word_list)
    
    # Game variables
    guessed_letters = []
    guesses_left = 6
    
    print("Welcome to Hangman!")
    print("Try to guess the secret  Fruits Name.")

    # 2. while loop to keep the game running
    while guesses_left > 0:
        # Build the current state of the word using lists and strings
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
                
        # Check for win condition
        if "_" not in display:
            print(f"\nCongratulations! You guessed the word: {word}")
            break

        # Display current status
        print(f"\nWord: {display.strip()}")
        print(f"Guesses remaining: {guesses_left}")
        if guessed_letters:
            print(f"Letters guessed: {', '.join(guessed_letters)}")
            
        # Get user input
        guess = input("Guess a letter: ").lower()

        # Input validation using if-else
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter. Try a different one!")
            continue

        # Add the valid guess to our list of guessed letters
        guessed_letters.append(guess)

        # 3. Limit incorrect guesses to 6
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guesses_left -= 1

    # Loss condition (while loop finishes because guesses_left == 0)
    if guesses_left == 0:
        print(f"\nGame Over! You ran out of guesses. The word was: '{word}'")

if __name__ == "__main__":
    play_hangman()