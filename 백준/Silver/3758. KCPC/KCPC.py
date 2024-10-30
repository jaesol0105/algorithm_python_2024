T = int(input())
for _ in range(T):
    n, k, t, m = list(map(int,input().split())) #팀수 문제수 내팀번 엔트리수
    score = [[0]*(k+3) for _ in range(n+1)] #팀번호(0) 점수(1~k+1) 제출(k+2) 시간(k+3)
    for i in range(n + 1): #팀번호
        score[i][0] = i
    for time in range(m): #10,000
        i, j, s = list(map(int,input().split())) #팀번 문제번 점수
        score[i][j] = max(s,score[i][j])
        score[i][-2] += 1
        score[i][-1] = time
    score = sorted(score[1:], key= lambda x : (-sum(x[1:k+1]),x[k+1],x[k+2])) #팀별 점수 합, 제출수, 마지막 제출시간
    for i in range(len(score)):
        if score[i][0] == t:
            print(i+1)
