n = int(input())
start = []
end = []
for _ in range(n):
  s, e = list(map(int, input().split()))
  start.append(s)
  end.append(e)

def find_next(k):
  ss = [i for i, v in enumerate(start) if v == k]

  se = 9999
  for i in range(len(ss)):
    if end[ss[i]] < se:
      se = end[ss[i]] # start의 최소값인 index들 중 end의 최소값 (start[ss[i]], se)

  return ss[i] # 결국 최소값인 index

index = find_next(min(start)) # 시작
