# Day 11: Functional Tools in Python

# 1. Lambda Function
# Anonymous function used for short, simple functions.
square = lambda x: x * x
print("Lambda Square of 5:", square(5))

# 2. zip()
# Combines multiple iterables element-wise.
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
zipped = zip(names, scores)
print("Zip Output:", list(zipped))

# 3. enumerate()
# Adds a counter to an iterable.
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits, start=1):
    print(f"Fruit {idx}:", fruit)

# 4. map()
# Applies a function to every item in an iterable.
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print("Map Squared:", squared)

# 5. filter()
# Filters elements based on a function (returns True or False).
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Filter Even:", even_nums)

# 6. reduce()
# Applies a rolling computation to sequential pairs of values.
from functools import reduce
sum_all = reduce(lambda x, y: x + y, nums)
print("Reduce Sum:", sum_all)
