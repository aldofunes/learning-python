first_name = input("What is your first name?  ")
age=int(input("What is your age?   "))
print("Hello,", first_name) 
print(first_name, "is learning Python")


if first_name=="karen":
    print("me encanctò el fin de semana")
elif first_name=="aldo":
    # Alguien menr quizas no sabe leer
    if age<6:
        print("Aprende a leer")
    print("eres un tonto, {}".format(first_name))
else:
    print("gracias por visitar, {}, y te {}.".format(first_name, "odio"))