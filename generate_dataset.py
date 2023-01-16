# generate a random dataset of size set_size with values ranging between biggest and smallest
import random

file = "data.csv"
set_size = 1000

biggest = 500
smallest = 0

dataset = ""

for i in range(set_size):
    dataset += str(random.randint(smallest, biggest))
    if i != set_size - 1:
        dataset += ","

with open(file, "w") as f:
    f.write(dataset)









