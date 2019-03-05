
# 1. Consider the following code:

```python
all_restaurants = [
    "Taco City",
    "Burgertown",
    "Tacovilla",
    "Hotdog station",
    "House of tacos",
]

def tacos_only(restaurants):
    taco_joints = restaurants.copy()
    for taco_joint in taco_joints.copy():
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
    return taco_joints

dinner_options = tacos_only(all_restaurants)
```

Why do you think the author used the copy method in the for loop here:

```python
    for taco_joint in taco_joints.copy():
```

  a  It follows the indices through iteration, using only valid elements of immutability reference, but sequential.

  b  It is unnecessary, copy creates an identical copy of the list.

  c  Modifying a list while looping through it is discouraged as it will produce unexpected results. This code is looping through a copy and then modifying the original.

# 2. Consider the following code:

```python
turtles = [
    "Michelangelo",
    "Leonardo",
    "Raphael",
    "Donatello",
]

def shredder(names):
    if len(names) >= 1:
        names[0] = "Bebop"

shredder(turtles)

for turtle in turtles:
    print("* " + turtle)
```

What would the output be?

    A

    * Bebop
    * Leonardo
    * Raphael
    * Donatello

    B

    * Michelangelo
    * Leonardo
    * Raphael
    * Donatello

    C

    * Donatello
    * Raphael
    * Leonardo
    * Michelangelo

Report Question 