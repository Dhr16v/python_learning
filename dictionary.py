# 5️⃣ DICTIONARY
# 👉 Definition

# A dictionary stores data in key-value pairs.
# It is mutable, unordered, and unique in keys.

student = {
    "name": "Dhruv",
    "age": 21,
    "course": "BCA"
}

# Accessing values
print(student["name"])
print(student.get("course"))

# Adding & updating values
student["age"] = 22
student["city"] = "Ahmedabad"

print(student)

# Removing keys
student.pop("city")
print(student)

# Loop through dictionary
for key, value in student.items():
    print(f"{key} → {value}")

print(student.keys())      # dict_keys(['name', 'age', 'course'])
print(student.values())    # dict_values(['Dhruv', 22, 'BCA'])
print(student.items())     # dict_items([...])

# Nested Dictionary Example

students = {
    1: {"name": "Dhruv", "age": 21},
    2: {"name": "Raj", "age": 20}
}

print(students[1]["name"])   # Dhruv
print(students[2]["age"])    # 20
