programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over nad over again.", # end with a comma so you can add more items to the dictionary
} # ending curcly bracket should go at the start of the dictionary

print(programming_dictionary["Bug"]) #providing the key so that we can return the value associated with it

#adding new items to the dictionary
programming_dictionary["Cartman"] = "fatass jew hater"

print(programming_dictionary) # printing the contents of the dictionary

empty_dictionary = {} #creating an empty dictionary to add to it later

# programming_dictionary = {} #now the programming dictionary is empty as we have set it to be empty

programming_dictionary["Bug"] = "This is an edited dictionary item" # finds the value of bug and changes it, if there is no value of "bug" it will create it

for key in programming_dictionary:
  print(key) # printing all the keys in the dictionary
  print(programming_dictionary[key]) # pritning the key and the associated value


##############################
capitals = {
  "france": "Paris",
  "Germany": "Berlin",
}

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12,}, #nesting a dictionary inside of a dictionary along with a value for visits
  "Germany": {"german_cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "germany_total_visits": 15}, # you can nest a list inside of a dictionary too
}                                                                                                            



#nesting a dictionary inside a list
travel_log = [
  {"country": "France", 
   "cities_visited": ["Paris", "Lille", "Dijon"], 
   "total_visits": 12
  }, 
  {"country": "Germany",
   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
   "total_visits": 15
  },
]
