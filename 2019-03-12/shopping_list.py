groceries_list = []


def show_help():
    print("Groceries")
    print("""
Enter an item to add to the groceries list

Enter "DONE" when finished.
Enter "HELP" for this help.
Enter "VIEW" to show the list.
""")


def add_item_to_list(item):
    groceries_list.append(item)

def final_list():
    print("Your list is: ")
    for item in groceries_list:
        print("* ", item)


show_help()
while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        final_list()
        break

    elif new_item == "HELP":
        show_help()
        continue
        
    elif new_item == "VIEW":
        final_list()
        continue

    # Call function to add the inputted item to our list
    add_item_to_list(new_item)
    length= len(groceries_list)
    print("The length of your list is: ", length)

