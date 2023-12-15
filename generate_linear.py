# generate a shuffled dataset where every number is unique, linear
import random
file = "data.csv"

biggest = 1000
smallest = 1

nums = [str(i) for i in range(smallest, biggest + 1)]

random.shuffle(nums)

dataset = ",".join(nums)

with open(file, "w") as f:
    f.write(dataset)
