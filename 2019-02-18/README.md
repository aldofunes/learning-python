# Loops

Loops are blocks of code that repeat while a statement is true and when we have
a list an we want to repeat some code for each element of that list

## While Loop

> While this condition is true, run this code

```python
password = input("Please enter a super secret password:  ")

while password != "opensesame":
    password = input("Invalid pasword, try again:  ")
```

This block of code will check if the pasword entered by the user is different
from `opensesame`, and while it is different, it will prompt the user to
reenter the password and start again.


## For loops

For every item in this object, run this code.

```python
banner = "Happy Birthday!"

for letter in banner:
    print(letter.upper())
```

This code will print the uppercase version of every character in the string `banner`.

See the difference?

For loops only run until the end of the `iterable`, the while loop checks if a
condition is true and then runs the code.

__What are iterables__
Item that we are able to iterate on. A string is a list of characters; we can
do something for a character, and ask the iterable for the next on to iterate on.
