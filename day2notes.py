#Data Types

# String
"Hello"
# always start counting at 0 instead of 1
print("Hello"[0])
print("Hello"[4])
print("Hello"[1])

# Integer
# whole number without any decimal places

print(123 + 345)

# you can visualize large numbers by adding an underscore underneath, the computer will ignore it
print(123_456_789)

# float
3.14159

# boolean

True
False

# this fucntion checks wwhat you put in the parenthesis and checks wht data type it is
num_char = len(input("what is your name?"))
print(type(num_char))

# change a data type from one type to another
num_char = len(input("what is your name?"))

new_num_char = str(num_char)  # converts an integer to string datatype

print("your name has " + new_num_char + " characters")

print(70 + float("100.75"))

print(str(434) + str(3784))

#CONVERT UR TYPES BRUH
# 🚨 Don't change the code below 👇
two_digit_number = input(
    "Type a two digit number: ")  # takes 2 digit number input as a string
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
num1 = int(two_digit_number[0])  #these two lines convert the first and second digits from strings to integers
num2 = int(two_digit_number[1])

num3 = num1 + num2  # add integers together to make the result
print(num3)  # prints the result of the first two digits adding together

# operators , these also follow PEMDAS , between mult & div, add and sub whiever is the most left gets executed first
3 + 5
7 - 4
3 * 2
6 / 3
5**3  # ** raises the first number to an exponent, in this case this would be 5^3

# if you input a float as a string, you have to convert it to a float bc if you convert to an int it will give an error
# new_height = float(height)
# new_weight = float(weight)

#rounding up floats
print(int(8/3))

#using round function you can round numbers up or down
print(round(8/3))

#prints out 3 since 2.6 rounds up to 3
print(round(8/3 , 5)) # the ,5 in the round function dictates how many decimal places itwill round to

# using // you can automatically get rid of all numbers after decimal and convert to int
print(round(8 // 3))

result = 4 / 2 
result /= 2 #the /= is dividing the result that you get from the previous line in half again, outputting 1
print(result) # this will output 1

score = 0
# user scores a point
score += 1 #this will allow score to be increased by 1 every time, can also be used with - , * , /  for the same effects as the operator
print(score) # outputs 1

score_2 = 0
height = 1.8
isWinning = True
# print("your score is " + score_2) <- this gives an error
# f-string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}") # f string allows us to not have to convert data types, put the variable you want to output inside {}

# float_percent_tip /= 10. shifts decimal place left, *= 10 shifts it to the right ne place