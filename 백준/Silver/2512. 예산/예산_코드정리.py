N= int(input())
num_list = list(map(int,input().split()))
M= int(input())

start = 1
end = max(num_list)
result = -1
while start<=end:
    mid = (start+end)//2
    if sum([mid if num > mid else num for num in num_list]) <= M: # 남거나 같을때
        result = mid
        start = mid + 1
    else: # 부족할때
        end = mid - 1

print(result)
