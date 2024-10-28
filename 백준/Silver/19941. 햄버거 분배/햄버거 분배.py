N, K =  list(map(int,input().split()))
S = list(input())

cnt =0
for i in range(len(S)):
    if S[i] == 'P':
        for j in range(-K, K+1):
            if i+j>=0 and i+j<len(S):
                if S[i+j] == 'H':
                    cnt += 1
                    S[i+j] = 'O'
                    break

print(cnt)
