# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_combo = (name1 + name2).lower()
t = name_combo.count('t')
r = name_combo.count('r')
u = name_combo.count('u')
e = name_combo.count('e')
true_count = t + r + u + e

l = name_combo.count('l')
o = name_combo.count('o')
v = name_combo.count('v')
e = name_combo.count('e')
love_count = l + o + v + e

score = int(str(true_count) + str(love_count))

if score < 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
