names = ['Aamir', "kalimi", 'how are you', 'Aamir', 3]
# print(type(names))
# print(names[3])
# print(len(names))
# print('kalimi' in names)
# print(names)
# print(type(names[4]))
# for name in names:
#     print(type(name))
#     if type(name) == 'str':
#         print(name.upper())
#
# for i in range(len(names)):
#     print(names[i])
# print("*************************")
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1
# print("*************************")

# [print(x) for x in names]
# action variable for in list
myNames = [str(x) for x in names]
# print(myNames)
# names.sort()
myNames.sort()
print(names)
print(myNames)
copyList = names.copy()
copyList.append(4)
print(copyList)
copyList.extend(myNames)

