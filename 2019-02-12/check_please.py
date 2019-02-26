import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("Cannot split in that number of people")
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person


try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Invalid value received.")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))
