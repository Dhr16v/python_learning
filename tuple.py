# TUPLE
# 👉 Definition

# A tuple is like a list but immutable (cannot change elements once created).
# Written in parentheses ().

my_tuple = (10, 20, 30, 40)

print(my_tuple[0])     # 10
print(my_tuple[-1])    # 40

# Tuple unpacking
a, b, c, d = my_tuple
print("a =", a, "b =", b, "c =", c, "d =", d)

# Tuple methods
print(my_tuple.count(20))   # count occurrences
print(my_tuple.index(30))   # find index of value
