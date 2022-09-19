# 백준 1026번

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = 0

a.sort()

for i in a :
    result += i * max(b)
    b.remove(max(b))

print(result)