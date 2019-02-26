# Booleans

Named after George Boole

- 1     /   0
- True  /   False
- On    /   Off

## Open the REPL (python shell)

Run:

```python
"taco" in "catacombs"
```

You can also coerce values

```python
bool(0)
bool(1)
```

## Truthy and falsey

Any non-zero number is `True`

```python
bool(24)
bool(-1)
```

Any non-empty string is `True`

```python
bool("burrito")
bool(" ")
bool("true")
bool("false")
```

An empty string is `False`

> Emptyness is falsey

```python
bool("")
```

## Operations

Negate a Boolean with `not`

Chain Booleans with `and` & `or`

Use `()` to order operations

```python
(False or False or True) and not (True and False)
```

__Quiz 1__

## Comparing values

Use one `=` for assigning values to variables, and two `==` for comparing values

```python
# store the string 'apples' in the variable 'fruit'
fruit = "apples"

# is the variable 'fruit' equal to 'apples'
fruit == "apples"

# is the variable 'fruit' equal to 'oranges'
fruit == "oranges"
```

## Conditionals

> If I am tired and feeling lazy, I go to sleep

Python uses the keywords: `if`, `else`, and `elif` con branching or conditional logic

__Challenge 1__

## Other operators

Try out these lines in the shell

```python
"elotes" != "esquites"

"elotes" < "esquites"

6 > 3

24 <= 24
```
