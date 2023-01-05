scores = []
studentAndScore = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    studentAndScore.append([name, score])
    scores.append(score)

secLow = sorted(set(scores))[1]
results = sorted([student[0] for student in studentAndScore if student[1] == secLow])

print(scores)
print(studentAndScore)
print(secLow)
print(*results, sep='\n')
