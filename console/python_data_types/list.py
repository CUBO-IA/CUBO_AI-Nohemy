# list.py
# LIST - an ordered, changeable collection

# 1. Creating a list
fruits = ["apple", "banana", "orange"]

print(fruits)

# 2. Accessing elements
print(fruits[0])
print(fruits[-1])

# 3. Changing an element
fruits[1] = "grape"
print(fruits)

# 4. Adding elements
fruits.append("mango")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

# 5. Removing elements
fruits.remove("apple")
print(fruits)

last_fruit = fruits.pop()
print("Removed:", last_fruit)
print(fruits)

# 6. Useful operations
numbers = [5, 2, 8, 1]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))

numbers.sort()
print(numbers)

# 7. Check the data type
print(type(fruits))

# Practice:
# Create a list of 5 favorite foods.
# Add one food, remove one food, and print the final list.
