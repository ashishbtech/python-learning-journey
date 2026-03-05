# dict_operations.py

student = {"name": "Bob", "grade": "A"}

# Adding new key-value
student["age"] = 20

# Updating
student["grade"] = "A+"

# Removing
del student["age"]

print("Updated student dictionary:", student)

# Looping through dictionary
for key, value in student.items():
    print(f"{key}: {value}")