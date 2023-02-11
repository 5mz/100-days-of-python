#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total_bill = input("What was the total bill? " )
float_total_bill = float(total_bill)

percent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
float_percent_tip = float(percent_tip)
float_percent_tip /= 10.
float_percent_tip /= 10.
float_percent_tip = float_percent_tip + 1

split = input("How many people to split the bill? ")
float_split = float(split)

actual_payment = round((float_total_bill * float_percent_tip) / (float_split) , 2)
print(f"Each person should pay {actual_payment}")
