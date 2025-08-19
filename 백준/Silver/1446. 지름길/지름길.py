n,d = list(map(int,input().split()))
rlist = [list(map(int,input().split())) for _ in range(n)]
ans = [i for i in range(d+1)]

for i in range(d+1):
    if i > 0:
        ans[i]= min(ans[i], ans[i-1]+1)
    for sta, end, distance in rlist:
        if sta == i and end <= d: #지름길이있고, 목적지앞까지면
            ans[end]= min(ans[i]+distance, ans[end])

print(ans[d])