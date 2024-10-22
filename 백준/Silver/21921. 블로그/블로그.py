N, X = list(map(int,input().split()))
num_list = list(map(int,input().split()))

sum_of_num = sum(num_list[:X])
max_of_num = sum_of_num
cnt = 1
for i in range(X, len(num_list)):
    sum_of_num += num_list[i]-num_list[i-X]
    if sum_of_num > max_of_num:
        max_of_num = sum_of_num
        cnt = 1
    elif sum_of_num == max_of_num:
        cnt +=1

if max_of_num == 0:
    print("SAD")
else:
    print(max_of_num)
    print(cnt)