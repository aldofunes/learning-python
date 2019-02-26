# Quiz 1

## 1. What would the output of this script look like?

```python
def display_blanks(word):
    blanks = "-" * len(word)
    print(blanks)

print("Puzzle 1:")
display_blanks("treehouse")
print("Puzzle 2:")
display_blanks("python")
```

Answer:
A. Nothing this code will not work. It violates the D.R.Y. principle.

B. 
```
Puzzle 1:
---------
Puzzle 2:
------
```

C. 
```
Puzzle 1:
-
Puzzle 2:
-
```


## 2. What is the missing keyword?
```python
_____ whisper(text):
    print(text.lower())
```

Answer:
```
def
```

## 3. There is a code smell in the code below:

```python
first_number = 5
first_result = first_number * first_number
print("The number {} squared is {}".format(first_number, first_result))

second_number = 8
second_result = second_number * second_number
print("The number {} squared is {}".format(second_number, second_result))
```

**What could be done to fix the duplication of code?**


A. Create a function and have it accept a parameter of a number to square

B. There is nothing wrong with this code. If there is a change needed, it's simple to just update the code.

C. Do not use variable names that have order in them

