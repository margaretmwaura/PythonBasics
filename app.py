# For this to work when run one must install the debug run extension
# The variable name does not require a syumbol before the name of the variable
# We cannot use a + while concantenating intergers hence we use comma
# Backslash is used for special characters
# using from means import
from math import *

name = "margaret"
age = 25
print("My name is " + name + " \nand she is " , age ," years old")
print(name.capitalize().islower())
print(len(name))
print(name.index('g'))
print(name.replace('a','i'))
sum = 25 + 29
print(sum)
print(20%6)
number = str(35)
print("I want to be rich at the age of " + number)
print(abs(- 25))
print(max(4, 2))
print(min(4, 2))
print(round(3.2))
print(bin(344))
print(sqrt(100))