# string.py
# STRING (str) - text

# 1. Creating strings
name = "Alex"
message = 'Hello, Python!'

print(name)
print(message)

# 2. Joining strings
first_name = "Alex"
last_name = "Smith"

full_name = first_name + " " + last_name
print(full_name)

# 3. f-strings
age = 16
print(f"My name is {name} and I am {age} years old.")

# 4. Useful string operations
text = "Python is fun"

print(text.upper())
print(text.lower())
print(len(text))
print(text.replace("fun", "powerful"))

# 5. Accessing characters
word = "Python"

print(word[0])   # P
print(word[1])   # y
print(word[-1])  # n

# 6. Check the data type
print(type(name))

# Practice:
# Create a string with your name and print:
# - the name in uppercase
# - the name in lowercase
# - its length
