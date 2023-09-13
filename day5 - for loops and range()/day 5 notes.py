#loops
fruits = ["apple", "peach", "pear",] #the loop will print things for however many items are in the fruits list, if there was 6 items it would loop 6 times etc
for fruit in fruits:
  print(fruit) #this function prints out each item in the list fruits, also assigns fruit as a variable to the items in the list and that is why it is able to print things out
  print(fruit + " pie") #this prints the item in the list + pie, because it goes line by line and then restarts the loop, until it is done with the list

# max() will give you the highest value inside of a list, while min() will give you the lowest value

#for loops with range

for number in range (1,10): # this will give you all numbers between 1 and 9 but not 10, if you want 10, you have to set the range to 1,11
  print(number)
for number in range (1,11):
  print(number)
for number in range (1,11,3): # this will give us the numbers 1-10, but the 3 indicates that it will go up in incriments of 3 instead of 1 (default value) you can change the 3 to any number
  print(number)
total = 0
for number in range (1,101): #adds together all values from 1 to 100
  total += number
print(total)

