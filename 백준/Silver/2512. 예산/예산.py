N= int(input())
num_list = list(map(int,input().split()))
M= int(input())

if sum(num_list) > M:
    start = 1
    end = max(num_list)
    while True:
        mid = (start+end)//2
        if start == mid:
            print(mid)
            break
        if sum([mid if num > mid else num for num in num_list]) <= M: # 남거나 같을때
            start = mid
        else: # 부족할때
            end = mid

else:
    print(max(num_list))