n,d = list(map(int,input().split()))
rlist = [list(map(int,input().split())) for _ in range(n)]
ans = [i for i in range(d+1)]

for i in range(d+1):
    if i > 0:
        ans[i]= min(ans[i], ans[i-1]+1)
    for sta, end, distance in rlist:
        if sta == i and end <= d and ans[end] > ans[i]+distance:
            ans[end]= ans[i]+distance

print(ans[d])