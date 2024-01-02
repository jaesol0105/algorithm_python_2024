import sys
input = sys.stdin.readline

while True:
  a,b,c = map(int,input().split())
  if a+b+c == 0:
    break
  if a+b+c - max(a,b,c) <= max(a,b,c):
    print("Invalid")
    continue
  if a == b or b == c or a == c:
    if a == b and b == c:
      print("Equilateral")
      continue
    print("Isosceles")
    continue
  print("Scalene")
