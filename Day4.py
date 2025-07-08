# For loop examples
print("For loop: Print numbers from 1 to 5")
for i in range(1, 6):
    print(i)  # prints numbers 1 to 5

print("\nFor loop: Print each fruit in the list")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)  # prints each fruit

print("\nFor loop: Sum of numbers in a list")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num  # add each number to total
print("Sum is:", total)

print("\nFor loop: Multiplication table of 3")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

# While loop examples
print("\nWhile loop: Print numbers from 1 to 5")
i = 1
while i <= 5:
    print(i)  # prints numbers 1 to 5
    i += 1  # increment i by 1

print("\nWhile loop: Calculate factorial of 4")
n = 4
factorial = 1
count = 1
while count <= n:
    factorial *= count  # multiply factorial by count
    count += 1  # increment count
print(f"Factorial of {n} is {factorial}")

print("\nWhile loop: Reverse a string")
s = "hello"
index = len(s) - 1
reversed_str = ""
while index >= 0:
    reversed_str += s[index]  # add characters from end
    index -= 1  # move index backward
print("Reversed string:", reversed_str)

print("\nWhile loop: Simple guessing game")
secret = 7
guess = int(input("Guess the secret number between 1 and 10: "))
while guess != secret:
    print("Wrong guess! Try again.")
    guess = int(input("Guess again: "))
print("Congratulations! You guessed it.")
