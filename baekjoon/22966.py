n = int(input())
a = [] 
for i in range(n):
    a.append(input().split())
a = sorted(a, key= lambda x:x[1])
print(a[0][0])
