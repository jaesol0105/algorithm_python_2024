import sys
input = sys.stdin.readline

N,M = list(map(int, input().split()))
grade = []
for _ in range(N):
    name, score = list(input().split())
    grade.append((int(score),name))
for _ in range(M):
    target = int(input())
    start = 0
    end = len(grade) - 1
    result = 0
    while start<=end:
        mid = (start+end) //2
        if grade[mid][0] >= target:
            result = mid
            end = mid - 1
        else:
            start = mid +1
    print(grade[result][1])
