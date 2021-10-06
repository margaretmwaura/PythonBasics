list1 = [4, 3, 5, 1, 2]
list2 = ['oranges', 'mangoes', 'bananas', 'pineapples', 'apples', 'bananas']
list1.extend(list2)
print(list1)
list2.append('cherry')
print(list2)
print(len(list2))
list2.insert(1, 'passion')
print(list2)
list2.remove('mangoes')
print(list2)
# list2.clear()
print(list2.index('bananas'))
print(list2.count('bananas'))
list3 = [4, 3, 5, 1, 2]

list3.reverse()
print(list3)

list3.sort()
print(list3)

list4 = list3.copy()
print(list4)

list4.pop()
print(list4)

print(list2)
list2.pop(4)
print(list2)

del list3
print(list3)