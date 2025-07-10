# List Examples: Mutable, Ordered, Duplicates Allowed, Mixed Data Types

# Creating a list
my_list = ["apple", "banana", "cherry"]
print("Original List:", my_list)

# Lists are ordered (indexed)
print("First item:", my_list[0])

# Lists are mutable (changeable)
my_list[1] = "blueberry"
print("After changing second item:", my_list)

# Adding items
my_list.append("mango")
print("After appending:", my_list)

# Lists allow duplicates
my_list.append("apple")
print("After adding duplicate:", my_list)

# Lists can store mixed data types
mixed_list = ["Python", 3.14, True, 42]
print("Mixed data types in list:", mixed_list)

print("\n" + "-"*40 + "\n")

# Tuple Examples: Immutable, Ordered, Duplicates Allowed, Mixed Data Types

# Creating a tuple
my_tuple = ("red", "green", "blue")
print("Original Tuple:", my_tuple)

# Tuples are ordered
print("Second item:", my_tuple[1])

# Tuples are immutable - cannot change items
# Uncommenting the line below will raise an error
# my_tuple[1] = "yellow"  # ❌ Error

# Tuples allow duplicates
dup_tuple = ("apple", "apple", "banana")
print("Tuple with duplicates:", dup_tuple)

# Tuples can store mixed data types
mixed_tuple = ("text", 99, False, 5.5)
print("Mixed data types in tuple:", mixed_tuple)
