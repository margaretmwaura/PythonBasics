country_file = open('countries.txt', 'r')

print(country_file.readable())
print(country_file.readline())
print(country_file.readline())
print(country_file.readlines()[-1])

for data in country_file.readlines():
    print(data)

country_file.close()