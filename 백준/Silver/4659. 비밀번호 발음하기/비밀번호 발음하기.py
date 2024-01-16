# 2024-01-16 15:11
import sys
input = sys.stdin.readline

while True:
  s = input().strip()
  if s == 'end':
    break

  flag = ' '
  rule_1 = 0
  rule_2 = [1 if s[i] in ['a','e','i','o','u'] else 0 for i in range(len(s))]
  for i in range(len(s)):
    if s[i] in ['a','e','i','o','u']:
      rule_1 += 1
    if i >= 2 and rule_2[i] == rule_2[i-1] == rule_2[i-2]:
      flag = ' not '
      break
    if i >= 1 and s[i] == s[i-1] and (s[i] not in ['e','o']):
      flag = ' not '
      break
  if(rule_1 == 0):
    flag = ' not '
  print('<' + s + '> is' + flag +'acceptable.')