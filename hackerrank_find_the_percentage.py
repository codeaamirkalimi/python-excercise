# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average = 0
total = 0
if query_name in student_marks:
    for score in student_marks[query_name]:
        total = total + score
    average = total / len(student_marks[query_name])
print('%.2f' % average)
