name_score = []
for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    name_score.append([score,name])

# print(name_score)
name_score.sort()
small = name_score[0][0]
while(name_score[0][0] == small):
    name_score.pop(0)

second_smallest = name_score[0][0]
while(name_score[0][0] == second_smallest):
    print(name_score[0][1])
    name_score.pop(0)
