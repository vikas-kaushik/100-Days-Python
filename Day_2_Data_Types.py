# The underscore helps us with number readability. Output is still 123456789
print(123_456_789)

# + operator concatenates strings. Output: 123456
print("123" + "456")

# String Subscripting
str1 = "Hello"
print(str1[0]) # H
print(str1[-5]) # H

# Float
print(3.14159)

# Boolean
print(True) # True
print(False) # False

############################################

# print(len(12345)) # error as len expects string, object of type 'int' has no len()

# Type Checking
print(type("hello")) # <class 'str'>
print(type(123)) # <class 'int'>
print(type(1.23)) # class 'float'
print(type(True)) # class 'bool'

# Type conversion
print(int("123") + int("456")) # 579

# bool to convert to boolean
print(bool("True"))


############################################
 # Mathematical Operators

print(type(6/3))  # Division always results in a float

print(5//3)  # Output is 1 (Strips off the decimal points)

print(6 + 4 / 2 - (1 * 2))


#PEMDAS : Parenthesis, Exponent, Multiplication, Division, Addition and Subtraction

name = 'Vikas'
age = 30
print(f"{name}'s age is {age}") # f strings help with manual type conversions