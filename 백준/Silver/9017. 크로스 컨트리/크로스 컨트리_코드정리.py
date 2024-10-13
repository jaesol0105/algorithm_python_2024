from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))
    num_cnt = [0] * (max(num_list)+1)

    for num in num_list:
        num_cnt[num] += 1

    team_score = defaultdict(list)

    num_list = [x for x in num_list if num_cnt[x] == 6]
    for idx, num in enumerate(num_list):
        team_score[num].append(idx+1)

    result = sorted(team_score.keys(), key= lambda x : (sum(team_score[x][:4]),team_score[x][4]))
    print(result[0])
