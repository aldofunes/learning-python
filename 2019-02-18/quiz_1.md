# 2. Considering the following code:

```python
request = input("What would you like?  ")
while "please" not in request:
    request = input("You seem to be missing a magic word.  What would you like?  ")
print("Here you go!")
```

__When will the user see the text "Here you go!" outputted?__

- A. Until the user yells in all capital letters.
- B. As soon as the request contains the string "please".
- C. This loop will never complete it is infinite.




# 1. Considering the following code:

```python
request = input("What would you like?  ")
while "please" not in request:
    request = input("You seem to be missing a magic word.  What would you like?  ")
print("Here you go!")
```

What would the output look like if the user inputted "milk please" to the first prompt?

- A You seem to be missing a magic word. What would you like?
- B Here you go!
- C SyntaxError

