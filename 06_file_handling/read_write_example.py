# read_write_example.py

# Append to a file
with open("example.txt", "a") as file:
    file.write("\nAdding a new line.")

# Read the file
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())