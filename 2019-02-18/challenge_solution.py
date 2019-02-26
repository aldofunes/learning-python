name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
response = input("{}, do you understand how Python loops work?  ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.
while response.lower() != "yes":
    print("While loops are block of codes that are executed while a condition is True.")
    print("")
    response = input("{}, do you understand Python loops now?  ".format(name))

  
# TODO: Outside the while loop, congratulate the user for understanding while loops
print("")
print("Hooray! It is great to read that you now understand Python loops! That was getting repetitive.") 
