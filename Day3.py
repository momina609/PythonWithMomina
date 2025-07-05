# ✅ 1. Function to Greet a User
print("First task")
def greet(name):
    print("Hello,", name)

greet("Momina")

print("Second task")
# ✅ 2. Function to Add Two Numbers
def add(a, b):
    return a + b

result = add(5, 7)
print("Sum:", result)

print("Third task")
 #✅ 3. Function to Check Even or Odd
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(10))  # Output: Even

print("Fourth task")
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # Output: 120

print("fifth task")
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(12, 45, 23))  # Output: 45

print("six task")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python is Amazing"))  # Output: 6





