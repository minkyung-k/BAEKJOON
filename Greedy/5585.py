# 백준 5585번

n = int(input())
change = 1000 - n
count = 0

coins = [500, 100, 50, 10, 5, 1]

for coin in coins :
    if change >= coin:
        count += change // coin 
        change %= coin
        if change <= 0 :
            break
    
print(count)