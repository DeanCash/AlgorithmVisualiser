# generate a dataset from smallest going up to biggest, linear

file = "data.csv"

biggest = 500
smallest = 0

nums = []

string = []
for i in range(biggest, smallest, -1):
    string.append(str(i))

with open(file, "w") as f:
    f.write(",".join(string))









