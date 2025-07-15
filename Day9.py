# -----------------------------
# Day 9 - Error Handling in Python
# -----------------------------

# Example 1: Basic try-except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")
except ValueError:
    print("❌ Error: Invalid input, please enter a number.")

# Example 2: Using else with try-except
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("❌ Please enter numbers only.")
else:
    print("✅ Age accepted:", age)

# Example 3: Using finally
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("❌ File not found.")
finally:
    print("🔁 Program tried to access the file.")

# Example 4: Raising a custom error
def divide(a, b):
    if b == 0:
        raise ValueError("❌ You can't divide by zero!")
    return a / b

try:
    print(divide(5, 0))
except ValueError as ve:
    print("Caught error:", ve)

# Example 5: Catching multiple errors
try:
    data = int("abc")  # causes ValueError
    x = 5 / 0           # causes ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print("Error caught:", e)

# Example 6: Creating your own exception class
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception!")
except CustomError as ce:
    print("⚠️ Custom Error:", ce)
