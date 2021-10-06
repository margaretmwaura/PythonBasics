'''
duplicates keys cannot be used , only one of such keys will be considered
The main distinction here is that arrows are not used and what is used is colons

'''

my_dict = {
    "name" : "tim",
    "nationality" : "african",
    "qualification" : "college",
    "age" : 25,
    "istall" : True,
    "friends" : ["Peter", "Paul", "Precious"]
}

print(my_dict['name'])
print(len(my_dict))
print(my_dict["age"])
print(my_dict["istall"])
print(my_dict["friends"])
print(type(my_dict))

i = 0

while i < 6 or i == 6:
    print(i)
    i = i + 1
print(i)

names = ['maggie','mag','jane','angie']

for name in names:
    print(name)

for x in "Hello":
    print(x)


for item in my_dict.values():
    print(item)

for item in my_dict.keys():
    print(item)

for x in range(8):
    print(x)
else:
    print("Finished looping")

for x in range(3, 8):
    print(x)
else:
    print("Finished range")

dimensionallist = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(dimensionallist[1][2])

for row in dimensionallist:
    for col in row:
        print(col)

for x in range(3):
    for y in range(3):
        print(dimensionallist[x][y])