# Day 1 - Variables and Data Types in Python
# Author: Momina Jabeen

# ----------------------------
# 🔹 What are Variables?
# ----------------------------
# Variables are used to store data in memory
# Python is dynamically typed — no need to declare type

# Example:
name = "Momina"        # str (string)
age = 20               # int (integer)
pi = 3.14              # float (decimal)
is_student = True      # bool (Boolean)
value = None           # NoneType (represents "no value")

# ----------------------------
# 🔹 Multiple Variable Assignment
# ----------------------------
x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)

# ----------------------------
# 🔹 Naming Rules
# ----------------------------
# Valid:
total_marks = 95
_my_variable = "Python"
# Invalid examples:
# 2marks = 50      ❌ Can't start with number
# total-marks = 80 ❌ Hyphen not allowed

# ----------------------------
# 🔹 Check Data Type
# ----------------------------
print(type(name))       # <class 'str'>
print(type(pi))         # <class 'float'>
print(type(is_student)) # <class 'bool'>
print(type(value))      # <class 'NoneType'>

# ----------------------------
# 🔹 Type Casting (Conversion)
# ----------------------------
a = "5"
b = int(a)       # Convert string to int
c = str(10)      # Convert int to string
d = float(3)     # Convert int to float

print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

# ----------------------------
# 🔹 Mutable vs Immutable Types
# ----------------------------
# Immutable types: cannot be changed after creation
x = 5             # int → immutable
name = "Momina"   # str → immutable

# Mutable types: can be changed
my_list = [1, 2, 3]  # list → mutable
my_list.append(4)
print("Updated List:", my_list)

# ----------------------------
# 🔹 Memory Management
# ----------------------------
# Python handles memory allocation automatically using Garbage Collection
