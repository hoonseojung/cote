import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  p = input().strip()
  n = int(input())
  arr = deque(input().strip()[1:-1].split(","))
  
  cur = 1

  if n < p.count('D'):
    print("error")
    continue

  for pp in p:
    if pp == 'R':
      cur *= -1
    elif pp == 'D':
      if cur < 0:
        arr.pop()
      else: arr.popleft()
  
  if cur < 0:
    arr.reverse()
  
  result = '['
  for i, a in enumerate(arr):
    if i != (len(arr)-1):
      result += str(a) + ','
    else: result += str(a)
  result += ']'
  
  print(result)