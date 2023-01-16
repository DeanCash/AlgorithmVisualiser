import random

file = "data.csv"

biggest = 500
smallest = 0

nums = []

# while len(nums) != biggest:
#     num = random.randint(smallest, biggest)

#     if str(num) in nums:
#         continue

#     nums.append(str(num))

# with open(file, "w") as f:
#     f.write(",".join(nums))

string = []
for i in range(biggest, smallest, -1):
    string.append(str(i))

with open(file, "w") as f:
    f.write(",".join(string))









