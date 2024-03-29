import random
from art import stages
from art import logo
from words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(logo)

while not end_of_game:
  
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    if guess not in chosen_word:
      print(guess + " is not in the word")
      lives -= 1
      if lives == 0:
        end_of_game += True
        print("You Lose.")
        print("The word was " + chosen_word)
        
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])
