# randomization , modules , lists
# random module https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# lists https://docs.python.org/3/tutorial/datastructures.html

import random #have to do this at the start of the code so that you can actually use the random function


rand_int = random.randint(1,10) #prints a random number between 1 and 10, and includes 1 and 10
print(rand_int)

# modules
# 
import my_module # importing variable and other things from the python file "my_module.py" on the left side

print(my_module.pi) #prints the value of the variable pi from my_module
print(my_module.piss) # you can reference any variable from another file by using {modulename}.{variable name} like shown to the left, and it will work

# making random floating point numbers
random_float = random.random()*5 #this will print a number between 0.0 and 1.0, but doesn't actually include 1.0, stops at 0.9999...  etc
print(random_float)

random_float * 5 # allows you to dictate and range of numbers, in this instance numbers will be from 0.0000.. to 4.9999...
print(random_float)

#instead of counting numbers in every single letter of a name you can just use a random number generator to make things easier
lovescore = random.randint(1,100)
print(f"Your love score is {lovescore}")


#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	 
#Write the rest of your code below this line 👇
side = random.randint(0,1)
if side == 1:
    print("Heads")
else:
    print("Tails")


# lists
# for example: fruits = [item1, item2] any variable attached to a pair of square brackets with any amount of items inside of it, and data type and they can even mix data types

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
print(states_of_america[0]) # prints out the very first option in the list, you can change the number in the square brackets to select any state you want
print(states_of_america[-1]) # starts counting from the end of the list, -1 would be hawaii because you can't have -0
states_of_america[1] = "pencilvania" # you are able to modify items from the list by referencing them and changing it like this

states_of_america.append("Ballsland") # .append() allows you to add a singlular option to the end of the list, in this case after hawaii
print(states_of_america)
states_of_america.extend(["Shitland", "Fartland", "Pissland"]) # using .extend() will alllow you to add multiple items to lists at the same time unlike .append()
print(states_of_america)

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# choosing a random integer between 1 and the length of how many names were entered in the initial prompt
spender = random.randint(1, len(names))

# using the random integer chosen above to match that with the number in the list of names as the index value, you have to -1 because to match counting starting at 0
finalchoice = names[spender - 1]

print(f"{finalchoice} is going to buy the meal today!")

# random.choice(a) will take a random choice from the list in the parenthesis 

# nested lists
fruits = ["Fruit1", "Fruit2", "fruit3",]
vegetables = ["vegtetables1", "vegetables2", "vegetables3",]
dirty_dozen = [fruits, vegetables] #this allows you to place both lists inside one overarching list 
print(dirty_dozen) # when you print the list you will see both lists and they will be separated by commas
print(dirty_dozen[1][2])
