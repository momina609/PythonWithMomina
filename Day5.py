# ✅ String Concatenation
# you can only conctenate strings with strings not with any integer.use str() function to convert a number to a string.
first_name = "Momina"
last_name = "Jabeen"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

age = 20
intro = full_name + " is " + str(age) + " years old."
print(intro)

# ✅ String Slicing
# rules
# syntax:text[start:stop:step]
# if the start index is null it means start from the first and if last index 
#is null it menas till end we go.
#from left to right the string start with index 0.
#from backward it start from index -1
# the value appers one less than the stop value.

text = "PythonProgramming"
print("Slice [0:6]:", text[0:6])
print("Slice [6:]:", text[6:])
print("Slice [:6]:", text[:6])
print("Last char:", text[-1])
print("Reversed:", text[::-1])

# ✅ String Methods
message = "  Python is Fun  "
print("Original:", message)
print("strip():", message.strip())#removes the extra space from the start and end of string.
print("upper():", message.upper())#convert string to capital letters
print("lower():", message.lower())# convert string to small letters
print("title():", message.title())#capitalize the first letter of every word in a string
print("replace():", message.replace("Fun", "Awesome"))# replace a part of string with another.
print("find('is'):", message.find("is"))#find the position(index) of the first occurrence of the substring
print("split():", message.split())#split the string into a list of words using spaces by default.
print("Length:",len(message))# returns the lenth if string in int