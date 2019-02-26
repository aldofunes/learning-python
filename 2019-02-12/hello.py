def yell(text):
    # We want to yell it to the user
    text = text.upper()
    # We also want as many exclamation marks as there are characters
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 8)
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't repeat yourself. Keep things DRY")

