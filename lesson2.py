# name = input('Enter your name : ')
# age = int(input('Enter your age : '))
# print("Your name is " + name + " and your age is " , age)

# userinput = input("Enter your gender : ")
# userinput = userinput.replace("boy", "girl")
# print(userinput)

name = "I am Maggie Mwaura"
age = 25
countries = ['Kenya','USA','UK',2, 'Australia']
print(countries)
print(countries[0][0])

# It will get the countries from the index specified to the end
print(countries[1 :])

# It will get the countries specified from the specified index to the last specified index
print(countries[1 : 3])

print(type(countries))
print(type(name))
print(type(age))

countries[0] = "United Kingdom"
print(countries)

# We want the last item
print(countries[-1])
print(len(countries))