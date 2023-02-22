# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
spender = random.randint(1, len(names))
finalchoice = names[spender - 1]
print(f"{finalchoice} is going to buy the meal today!")
