N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
gas = 0
cost = 0

for i in range(len(price)-1):
    if gas >= road[i]:
        gas -= road[i]
        continue
    cost += (road[i] - gas) * price[i]
    gas = 0
    for j in range(i+1, len(price)-1):
        if price[j] < price[i]:
            break
        else:
            cost += price[i] * road[j]
            gas += road[j]

print(cost)
