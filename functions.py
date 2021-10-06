# Get note of the identation, the braces and the colon, also note the spaces in identation are four spaces


def greetings_func(name):
    print("Hello " + name)

name = "Margaret Mwaura"
greetings_func(name)
greetings_func("Maggie")

def age_func(age):
    age = str(age)
    print("You are this old " + age)

age_func(25)

def user_details(name, age):
    print("Your name is " + name + " and you are " + str(age) + " years old")

user_details("Maggie", 25)
user_details(name = "Angeline", age = 46)

def class_students(*names):
    print(len(names))

class_students('Tim','Tom','Angela')
class_students('Tim','Tom','Angela','Lisa')


def marks():
    return 4 + 5

print(marks())

def sum_marks(num1, num2):
    return num1 + num2

# Thing to learn is that input is always a string so it is upon you to convert to an int or float 
# num1 = int(input('Enter the first value : '))
# num2 = int(input('Enter the second value : '))

# print(sum_marks(num1, num2))

# num1 = input('Enter the first value : ')
# num2 = input('Enter the second value : ')

# print(sum_marks(num1, num2))


def checkvalues(num1, num2):
    # In this case one can use is or ==
    # python uses and and or not && and ||
    if num1 == 2 and num2 == 4:
        print("The value is even")
    elif num1 is 4:
        print("The value is not 2 but it is even")
    else:
        print("The value is odd")

checkvalues(2, 4)
checkvalues(3, 1)
checkvalues(4, 5)


def checkTypeOfValues(number):
    rem = number%2
    if rem == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

checkTypeOfValues(2)
checkTypeOfValues(3)