# 🧮 4️⃣ SET
# 👉 Definition

# A set is an unordered collection of unique items (no duplicates).
# Written in curly braces {}.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Add and remove
set1.add(6)
set1.remove(3)

print("Set1:", set1)

# Set operations
print("Union:", set1 | set2)           # or set1.union(set2)
print("Intersection:", set1 & set2)    # or set1.intersection(set2)
print("Difference:", set1 - set2)      # in set1 not in set2
print("Symmetric Difference:", set1 ^ set2)
