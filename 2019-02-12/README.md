# Functions and loops

Encapsulate code logic in reusable places.

We have used some built-in functions 

- `print()`
- `len()`
- `bool()`
- `input()`

# DRY

Repeated and smelly code come from _copy pasta_, which is code that we copy,
paste and edit to accommodate a new scenario.

DRY means: Don't Repeat Yourself, and is one of the best practices to follow
when coding.

```python
praise = "You are doing great"
# We want to yell it to the user
praise = praise.upper()
# We also want as many exclamation marks as there are characters
number_of_characters = len(praise)
result = praise + "!" * number_of_characters
print(result)
```

Don't worry, there is a solution for that, functions and loops.

```python
def function_name(arguments):
    # Here goes the body of the function
    # It can span multiple lines
```

# Returned values

Some functions, like `len` return values, which we can assign to a variable.

We want to write a function that gives us the value of a split restaurant check.

```python
# TODO: Use the math module to round up the amount_due
def split_check(total, number_of_people):
    cost_per_person = total / number_of_people
    return cost_per_person
```

# Modules

Modules are collections of functions available to use. However, they must be
`import`ed before we can use them.

**Time to open the REPL** (python3 in your bash terminal)

[https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

```python
import math
math.ceil(20.24)

help(math)
```



# Error handling

Murphy's Law:
> Anything that can go wrong, will go wrong.

Translation:
> If a user can break our application, they will break it.

Unhandled errors are called exceptions, they are messy and not user friendly

For that, we use `try/except` blocks

## Raising exceptions

We can define and raise our own exceptional activity to be handled
