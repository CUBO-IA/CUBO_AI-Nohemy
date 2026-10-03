# dictionary.py
# DICTIONARY (dict) - stores data as key-value pairs

# 1. Creating a dictionary
person = {
    "name": "Alex",
    "age": 16,
    "country": "El Salvador"
}

print(person)

# 2. Accessing values
print(person["name"])
print(person["age"])

# 3. Adding a new key-value pair
person["student"] = True
print(person)

# 4. Changing a value
person["age"] = 17
print(person)

# 5. Removing a key-value pair
del person["country"]
print(person)

# 6. Useful methods
print(person.keys())
print(person.values())
print(person.items())

# 7. Check the data type
print(type(person))

# Practice:
# Create a dictionary about yourself with:
# name, age, favorite_subject, and city.
