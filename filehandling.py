# Day 10: File Handling in Python

# ✅ Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Momina!\n")
    file.write("This is Day 10 of Python.\n")

# ✅ Appending to the file
with open("example.txt", "a") as file:
    file.write("Appended line.\n")

# ✅ Reading the whole file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# ✅ Reading line by line
print("\nReading line by line:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# ✅ Using try-except for error handling
try:
    with open("non_existing_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("\n❌ File not found!")

# ✅ Using file.tell() and file.seek()
with open("example.txt", "r") as file:
    print("\nInitial position:", file.tell())
    file.read(5)
    print("Position after reading 5 chars:", file.tell())
    file.seek(0)
    print("After seek(0):", file.readline())
