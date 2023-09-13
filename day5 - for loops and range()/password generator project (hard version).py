#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = [] # converting password into a list so it can be shuffled, also empty so that it starts blank

for char in range(1, nr_letters + 1):    # we add a plus one so that the range includes all the letters the user wants, ex: an input of 4  would actually be 1-3, so we add +1 to get to 4
  password_list.append(random.choice(letters)) # you can either use .append or += to add to the password, they both do the same thing

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols) # we get a random symbol and it is being added to the password, works the same for all the other functions

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list) #shuffling the list of all gathered characters from the above functions


password = ""
for char in password_list: # adding each character in the list to a string, it gets it out of the [brackets] and into a normal string like vV45%6c!
  password += char

print(f"Your password is: {password}")
