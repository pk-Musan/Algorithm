N = int(input())
S = input()
T = ''

for n in range(N):
    if S <= S[::-1]:
        T = T + S[0]
        S = S[1:]
    else:
        T = T + S[-1]
        S = S[:len(S)-1]
        
print(T)