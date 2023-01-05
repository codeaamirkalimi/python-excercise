# newlist = [expression for item in iterable if condition == True]

# ages = [1, 2, 3, 4, 5]
# print("Ages", ages)
# newAge = [age for age in ages if age > 2]
# print("New Age", newAge)
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
n = int(input("n:"))

# result = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if x + y + z != n:
#                 result.append([i, j, k])
#
# print(result)

listCompResult = [[i, j, k]
                  for i in range(x + 1)
                  for j in range(y + 1)
                  for k in range(z + 1)
                  if (i + j + k) != n
                  ]
print(listCompResult)
