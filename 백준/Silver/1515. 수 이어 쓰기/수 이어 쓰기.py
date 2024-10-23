num_str = input()
num = 0
point = 0
while point < len(num_str):
    num += 1
    for c in str(num):
        if c == num_str[point]:
            point += 1
            if point == len(num_str):
                print(num)
                break