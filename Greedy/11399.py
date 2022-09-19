# 백준 11399번

n = int(input())
time = list(map(int, input().split()))

sum = 0

time.sort()

for i in range(n) :
    sum += time[i]
    for j in range(i) :
        sum += time[j]


print(sum)