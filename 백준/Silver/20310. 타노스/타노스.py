S = list(input())
for i in range(S.count('1')//2):
    S.remove('1')
S.reverse()
for i in range(S.count('0')//2):
    S.remove('0')
S.reverse()
print(''.join(S))