# set.py
# SET - an unordered collection of unique values

# 1. Creating a set
numbers = {1, 2, 3, 4}
print(numbers)

# Duplicate values are automatically removed
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

# 2. Adding elements
numbers.add(5)
print(numbers)

# 3. Removing elements
numbers.remove(2)
print(numbers)

# 4. Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# 5. Check the data type
print(type(numbers))

# Practice:
# Create two sets of numbers.
# Find their union and intersection.
