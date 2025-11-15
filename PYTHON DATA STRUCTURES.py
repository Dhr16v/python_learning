# 1️⃣ STRING
# 👉 Definition

# A string is a sequence of characters enclosed in single ' ' or double " " quotes.
# Strings are immutable (cannot be changed after creation).

# String creation
name = "Dhruv Gajjar"

# String indexing
print(name[0])     # D
print(name[-1])    # r  (last character)

# String slicing
print(name[0:5])   # Dhruv
print(name[6:])    # Gajjar
print(name[:5])    # Dhruv
print(name[::-1])  # reverse string



#string method learn
text = "  python programming  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace('python','java'))
print(text.split())

# String concatenation
a = "Hello"
b = "World"
print(a + " " + b)         # Hello World

# f-string formatting
age = 21
print(f"My name is {name} and I am {age} years old.")