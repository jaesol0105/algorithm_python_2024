import sys
input = sys.stdin.readline

p, m = list(map(int,input().split()))
q = []
for _ in range(p):
    level, nick = list(input().split())
    level = int(level)
    check = False
    for game in q:
        if game[0][0]-10 <= level <= game[0][0]+10 and len(game) < m:
            game.append((level,nick))
            check = True
            break
    if not check:
        q.append([(level,nick)])

for game in q:
    if len(game) == m:
        print('Started!')
    else:
        print('Waiting!')
    for level, nick in sorted(game, key= lambda x:x[1]):
        print(level, nick)