import random
from random import sample

random.seed(47)
print(random.random())
print(random.random())

animal=['cat', 'dog', 'horse', 'cow', 'chicken']
print(random.choice(animal))
print(sample(animal, 2))
print(animal)
random.shuffle(animal)
print(animal)

print(random.randint(2, 21))