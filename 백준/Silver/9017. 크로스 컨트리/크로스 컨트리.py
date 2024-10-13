T = input()

for i in range(int(T)):
    N = input()
    data = list(map(int,input().split()))

    # 자격이 있는 팀들 추리기
    team_score = dict()

    # 팀원 수 세기
    team_member_count = [0]*(max(data)+1)
    for j in range(len(data)):
        team_member_count[data[j]] += 1

    for j in range(1, len(team_member_count)):
        if team_member_count[j] == 6:
            team_score[j] = []

    # 팀 점수 기록 (6명 이상인 팀만)
    score = 1
    for team_of_player in data:
        if team_member_count[team_of_player] == 6:
            team_score[team_of_player].append(score)
            score += 1

    min_of_score = 9999
    five = 9999
    winner = -1
    
    # 우승 팀
    for key, value in team_score.items():
        if sum(value[0:4]) < min_of_score:
            winner = key
            min_of_score = sum(value[0:4])
            five = value[4]
        elif sum(value[0:4]) == min_of_score:
            if five > value[4]:
                winner = key
                five = value[4]

    print(winner)