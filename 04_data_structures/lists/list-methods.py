# list_methods.py

numbers = [1, 2, 3, 4]

# Adding elements
numbers.append(5)
numbers.insert(2, 10)

# Removing elements
numbers.remove(3)
popped = numbers.pop()  # removes last item

print("Updated list:", numbers)
print("Popped item:", popped)