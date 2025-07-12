# 🔸 Practice: Python Dictionaries and Sets 🔸

# -------------------------------
# ✅ 1. Dictionary: Create and Access
# -------------------------------
student = {
    "name": "Momina",
    "age": 20,
    "marks": 88
}
print("\n📌 Student Info")
print("Name:", student["name"])     # Access by key
print("Age:", student.get("age"))   # Using get method
print("Roll:", student.get("roll", "Not Assigned"))  # Default if key not found

# -------------------------------
# ✅ 2. Dictionary: Add/Update/Delete
# -------------------------------
student["grade"] = "A"     # Add new key
student["age"] = 21        # Update existing
del student["marks"]       # Delete key
print("\n📌 Updated Student:", student)

# -------------------------------
# ✅ 3. Dictionary: Looping
# -------------------------------
print("\n📌 Loop through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# -------------------------------
# ✅ 4. Dictionary: Nested Dictionary
# -------------------------------
students = {
    "s1": {"name": "Abeeha", "marks": 85},
    "s2": {"name": "Hina", "marks": 92}
}
print("\n📌 Nested Dictionary Example:")
for sid, info in students.items():
    print(f"{sid} → Name: {info['name']}, Marks: {info['marks']}")

# -------------------------------
# ✅ 5. Set: Create and Remove Duplicates
# -------------------------------
nums = [1, 2, 2, 3, 4, 4, 5]
unique = set(nums)
print("\n📌 Unique Numbers using Set:", unique)

# -------------------------------
# ✅ 6. Set: Add, Remove, Membership
# -------------------------------
colors = {"red", "green"}
colors.add("blue")
colors.discard("green")
print("\n📌 Modified Colors Set:", colors)
print("Is 'red' in set?", "red" in colors)

# -------------------------------
# ✅ 7. Set: Operations
# -------------------------------
a = {1, 2, 3}
b = {3, 4, 5}
print("\n📌 Set Operations:")
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference:", a ^ b)

# -------------------------------
# ✅ 8. Set Comprehension
# -------------------------------
squares = {x*x for x in range(1, 6)}
print("\n📌 Set Comprehension (Squares):", squares)

# -------------------------------
# ✅ 9. Dictionary + Set Combo Example
# -------------------------------
print("\n📌 Words appearing only once:")
words = ["apple", "banana", "apple", "kiwi", "banana", "grape"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

unique_words = {w for w in word_count if word_count[w] == 1}
print("Unique Words:", unique_words)
