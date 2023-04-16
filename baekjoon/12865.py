N, W = map(int, input().split())

bag_list = [[] * N for i in range(N)]
 
for i in range(N):
    n, w = map(int, input().split())
    bag_list[i] = (n, w)

bag_list.sort(key=lambda x: -x[1])

weight = 0
value = 0

for thing in bag_list:
    weight += thing[0]
    if weight > W:
        weight -= thing[0]
        continue
    else:
        value += thing[1]

print(value)
