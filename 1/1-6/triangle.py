N = int(input())
A = list(map(int, input().split()))
min_A = min(A)
answer = 0
triangle_length = 0
for n_a in range(N):
    for n_b in range(n_a+1, N):
        for n_c in range(n_b+1, N):
            triangle_length = A[n_a] + A[n_b] + A[n_c]
            if triangle_length < answer:
                break
            max_n = max([A[n_a], A[n_b], A[n_c]])
            if max_n < triangle_length - max_n:
                answer = triangle_length

if answer == 0:
    print("No")
else:
    print(answer)
                    
                    