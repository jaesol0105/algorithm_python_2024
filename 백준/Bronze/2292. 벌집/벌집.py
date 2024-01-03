n = int(input())
a, cnt = 1, 1
while n > a:
  a += 6*cnt
  cnt += 1
print(cnt)


'''
n = int(input())
k = 2
ak_ = 1

if n == 1:
  print(n)
  
else:
  while True:
    ak = ak_ + 6*(k-1)
    if ak >= n:
      print(k)
      break
    ak_ = ak
    k += 1
'''
