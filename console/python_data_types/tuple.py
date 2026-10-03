# tuple.py
# TUPLE - an ordered collection that cannot be changed

# 1. Creating a tuple
coordinates = (10, 20)
colors = ("red", "green", "blue")

print(coordinates)
print(colors)

# 2. Accessing elements
print(colors[0])
print(colors[-1])

# 3. Tuples can be unpacked
x, y = coordinates

print("x:", x)
print("y:", y)

# 4. A tuple cannot be changed
# coordinates[0] = 50  # This causes an error

# 5. Useful operations
print(len(colors))
print("red" in colors)

# 6. Check the data type
print(type(colors))

# Practice:
# Create a tuple containing the names of 3 countries.
# Print each country using its index.
