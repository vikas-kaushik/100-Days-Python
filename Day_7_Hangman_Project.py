import random

# Step 1 - Picking a Random Words and Checking Answers
word_list = ["aardvark", "baboon", "camel"]
lives = 6

# choose a random quiz word from the list
chosen_word = random.choice(word_list)
placeholder = '_'*len(chosen_word)
print(chosen_word)
print(placeholder)

# guess = input("Guess a letter: ").lower()

# Step 2 - Replacing Blanks with Guesses

# display = ""
#
# for letter in chosen_word:
#     if letter == guess:
#         display = display + letter
#     else:
#         display = display + "_"
#
# print(display)

# Step 3 - Checking if the Player has Won
# Step 4 - Keeping Track of the Player's Lives
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_letters:
        print(f"You have already chosen {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display = display + "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives ==0:
            print("Game Over")
            print("You Lose !!")

    if "_" not in display:
        game_over = True
        print("You Win !!")

