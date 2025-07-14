# 📘 Day 8: Python List & Dictionary Comprehension Practice

# ✅ List Comprehension Examples

# 1. Generate a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("1. Squares from 1 to 10:", squares)

# 2. Filter even numbers from a list
nums = [1, 4, 7, 10, 13, 16, 19]
evens = [x for x in nums if x % 2 == 0]
print("2. Even numbers:", evens)

# 3. Convert a list of strings to lowercase
names = ["Momina", "ALI", "Ayesha"]
lowercase_names = [name.lower() for name in names]
print("3. Lowercase names:", lowercase_names)

# 4. Add 5 to each number in a list
numbers = [10, 20, 30]
added = [n + 5 for n in numbers]
print("4. Numbers after adding 5:", added)

# 5. Get lengths of each word in a sentence
sentence = "Python is powerful"
word_lengths = [len(word) for word in sentence.split()]
print("5. Length of each word:", word_lengths)

# ✅ Dictionary Comprehension Examples

# 1. Create dictionary with numbers and their cubes
cubes = {x: x**3 for x in range(1, 6)}
print("6. Cubes dictionary:", cubes)

# 2. Count frequency of characters in a word
word = "banana"
char_count = {char: word.count(char) for char in word}
print("7. Character frequency in 'banana':", char_count)

# 3. Map fruit names to their lengths
fruits = ["apple", "banana", "kiwi"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print("8. Fruit name lengths:", fruit_lengths)

# 4. Create a dictionary of numbers and even/odd labels
labels = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
print("9. Even/Odd labels:", labels)

# 5. Swap keys and values of a dictionary
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("10. Swapped dictionary:", swapped)
