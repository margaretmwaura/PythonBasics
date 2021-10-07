one = int(input("Enter your first value : "))
two = int(input("Enter the second value : "))
op = input("Enter the operator : ")

# This makes it a global variable
result = 0

if op == '+':
    result = one + two
elif op == '-':
    result = abs(one - two)
elif op == '*':
    result = one*two
else:
    result = one/two

print(result)

try:
    x = int(input("Enter a value : "))
    print(x)
except:
    print("Something went wrong, please try again")
finally:
    print("We are done")