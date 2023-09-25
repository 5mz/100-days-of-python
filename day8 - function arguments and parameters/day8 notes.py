# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("Hello my name is cartman")
  print("Hello my name is keeeeenny")
  print("My name is stan and i loooove wendy")


def pass_greet(name): #name is the parameter
  print(f"Hello {name} how are you?")

greet()
pass_greet("Chloe") # this passes the name chloe as an argument into the function and into the variable "name" allowing it to be used inside of the function definition 
pass_greet("bob") # the name can be changed into whatever you want whenever the function is being called
pass_greet("cartman") # cartman is a argument

#functions with more than one input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"Your location is {location}. I am sending missles to your house shortly")

greet_with("Chloe","33 Silver Hill Court") # the first argument (Chloe) gets passed the the first parameter (name), the function takes into account the position of the arguments
greet_with("33 Silver Hill Court", "Chloe") # these are called positional arguments

#keyword arguments
def my_function(a,b,c):
  print(a)
  print(b)
  print(c)

my_function(a=1,b=2,c=3) # doesn't mater how you order these since we have assigned the variable inside of the argument area
greet_with(location = "Norway", name = "bob") # assigning the variables into the argument so that when it is passed to the parameters, so the order doesnt matter
