# 2024-01-17 11:20
import sys
input = sys.stdin.readline

n, game = input().strip().split()

played = set()
game_member = {'Y':2, 'F':3, 'O':4}

member, result = 1, 0

for i in range(int(n)):
  user_name = input().strip()
  if user_name not in played:
    played.add(user_name)
    member += 1
  if member == game_member[game]:
    member = 1
    result += 1

print(result)