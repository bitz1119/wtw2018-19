name_score = []
for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    name_score.append([score,name])

# print(name_score)
name_score.sort()
small = name_score[0][0]
kab_tak_smallest = 0
for i in name_score:
    if(i[0]==small):
        kab_tak_smallest = kab_tak_smallest+1
    else:
        break

second_smallest = name_score[kab_tak_smallest][0]
for i in range(kab_tak_smallest,len(name_score)):
    if(name_score[i][0] == second_smallest):
        print(name_score[i][1])
    else:
        break
