N = int(input())
m = int(input())
K = list(map(int, input().split()))
pick_num = 4

for n_a in range(N):
    for n_b in range(N):
        for n_c in range(N):
            for n_d in range(N):
                if K[n_a] + K[n_b] + K[n_c] + K[n_d] == m:
                    print(K[n_a], K[n_b], K[n_c], K[n_d])
                    print("Yes")
                    exit(0)

print("No")