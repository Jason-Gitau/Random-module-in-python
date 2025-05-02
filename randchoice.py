# The random module allows you to make random selections from a sequence (e.g., lists, tuples). This is incredibly useful for scenarios like picking a random item from a list or simulating random events.

import random

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Pick a random fruit from the list
print(random.choice(fruits))

# Pick 3 random fruits from the list, allowing duplicates
print(random.choices(fruits,k=3))   #the output is in form of a list

# Pick 3 random fruits from the list, without duplicates
print(random.sample(fruits,2))   #the output is in form of a list