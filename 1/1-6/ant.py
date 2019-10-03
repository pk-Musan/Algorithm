L = int(input())
n = int(input())
x = list(map(int, input().split()))
max_time, min_time = 0, 0

for x_n in x:
    #  すべてのアリは近い方の端へ向かうと考える
    min_time = max([min_time, min([x_n, L-x_n])])
    #  すべてのアリは遠い方の端へ向かうと考える
    max_time = max([max_time, max([x_n, L-x_n])])
    
print("min_time: {0}\nmax_time: {1}".format(min_time, max_time))