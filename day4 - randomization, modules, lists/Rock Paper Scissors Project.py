rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
art = [rock, paper, scissors,]

player_choice = int(input("Type 0 for rock, 1 for paper, or 2 for scissors.\n"))
if player_choice >= 3 or player_choice < 0:
  print("Invalid")
  quit()
print(art[player_choice])
computer_choice = random.randint(0,2)

print("Computer Chose:")
print(art[computer_choice])

print(player_choice)
print(computer_choice)

if player_choice == computer_choice:
  print("It's a tie!")
elif player_choice == 0 and computer_choice == 1:
  print("You lose!")
elif computer_choice == 0 and player_choice == 1:
  print("You lose!")
elif player_choice > computer_choice:
  print("You win!")
elif computer_choice > player_choice:
  print("You lose!")



