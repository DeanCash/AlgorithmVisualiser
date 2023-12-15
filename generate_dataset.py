# generate a random dataset of size set_size with values ranging between biggest and smallest
import random

file = "data.csv"

set_size = 1000

biggest = 500
smallest = 0

dataset = ",".join([str(random.randint(smallest, biggest)) for _ in range(set_size)])

with open(file, "w") as f:
    f.write(dataset)
