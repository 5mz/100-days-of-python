water_level = 50
if water_level > 80:
  print("drain water")
else:
  print("continue")

print("welcome to the rollerocaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("you can ride the rollercoaster")
else: 
  print("get taller lmao skill issue")

# > greater than , < less than, >= greater than or equal to , <= ess than or equal to, == equality, != not equal to
# == is checking the equality of two things, ratehr than a single = which assigns, if height == 120 is checking to see if height is exactly 120
# % modulo operator, divides a number by another number, and then it will give you the remainder 7 % 2, 2 + 2 + 2 + 1, two goes into 7 3 times with a remainder of 1, which will show up in the terminal
# odd numbers % 2 will always end up as remainder 1, while even numbers will always have a remainder of 0

#nested if else statement
# if ___:
#   if another condition:
#     do this
#   else:
#     do this
# else:
#   do this

if height >= 120:
  print("you can ride the rollercoaster")
  age = int(input("what is your age?"))
  if age >= 18:
    print("pay $7")
  else
else: 
  print("get taller lmao skill issue")


#elif condition, can make as many as you want between the if and else statement

if height >= 120:
  print("you can ride the rollercoaster")
  age = int(input("what is your age?"))
  if age < 12:
    print("pay $5 bucko")
  elif age <= 18:
    print("pay $7")
  else:
    print("pay your right lung")
else: 
  print("get taller lmao skill issue")

#nested if else using modulus to find the remainder to calculate if a year is a leap year or not
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#     else: 
#         print("Leap year.")
# else:
#     print("Not leap year.")

# bill += 3 is the same as bill = bill + 3, adding 3 to bill no matters what the value was before

#logicval operators
# a = 12
# not a > 15 is naturally false, but the not operator flips the outcome so now that statement is true
