# none.py
# NONE (NoneType) - represents the absence of a value

# 1. Creating a None value
result = None

print(result)
print(type(result))

# 2. None is useful when a value does not exist yet
username = None

print("Username:", username)

# Later, the variable can receive a value
username = "Alex"

print("Username:", username)

# 3. Check for None
value = None

if value is None:
    print("There is no value yet.")

# Practice:
# Create a variable called "answer" with None.
# Then change it to a number and print it.
