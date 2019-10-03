N = int(input())

ST = [list(map(int, input().split())) for n in range(N)]

work_num = 0
time = 0

for st in ST:
    if time < st[0]:
        time = st[1]
        work_num +=1

print(work_num)