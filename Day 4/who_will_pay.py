import random

friends=['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
print(random.choice(friends)) # random.choice() returns a random item from the list

#random.randint() returns a random integer between the two numbers
print(friends[random.randint(0, 4)])