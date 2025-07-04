#✅ 1. Age-based Voting Eligibility
print("First Practice Task")
age=int(input("Please enter your age:"))
if age>=18:
    print("you are eligible for voting")
elif age>0:
    print ("you are not eligible")
else:
    print("invalid age entered")

print("Second Practice Task")
#✅ 2. Simple Grading System
marks=int(input("Please enter your marks:"))
if marks>=90:
    print("grade is:'A+'")
elif marks>=80:
    print("grade is:'A'")
elif marks>=70:
    print("grade is:'B'")
elif marks>=60:
    print("grade is:'C'")
elif marks>=50:
    print("grade is:'D'")
else:
    print("fail")


print("Third Practice Task")
# ✅ 3. Number Checker (Positive, Negative, Zero)
num=int(input("Please enter a number:"))
if num>0:
    print("it is a positive number.")
elif num<0:
    print("it is a negative number.")
else:
    print("the num is zero")

print("Fourth Practice Task")
#✅ 4. Simple Login System   
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
elif username == "admin":
    print("Incorrect password.")
else:
    print("User not found.")

#✅ 5. Odd or Even Number
print("Fifth Practice Task")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

                                                   