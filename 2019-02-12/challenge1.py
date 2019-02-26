# Create a function named square. It should define a single parameter named number.
#
# In the body of the function, return the square of the value that was passed in.
#
# (A **square* is the value multiplied by itself. eg: The square of 5 is 25. 25 = 5 x 5)*

def square(number):
    new_value=number*number
    other = number*number*number
    return new_value
    
result=square(6)
print(result)

# Great now that you have created your new square method, let's put it to use.
#
# Under the function definition, call your new function and pass it the argument 3.
#
# Since your square function returns a value, create a new variable named result to store the value from the function call.



def square2(number):
    return number * number
    
result=square2(2)
print(result)
