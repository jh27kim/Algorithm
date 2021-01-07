Fee = list(map(int, input().split()))
arrival = [0 for i in range(3)]
depart = [0 for i in range(3)]

arrival[0], depart[0] = map(int, input().split())
arrival[1], depart[1] = map(int, input().split())
arrival[2], depart[2] = map(int, input().split())

arrival.sort()
depart.sort()
trucks = 0
answer = 0

for i in range(arrival[0], depart[2]):
    print(arrival, i, answer)
    if arrival != [] and i == arrival[0]:
        arrival.pop(0)
        trucks += 1
    elif i == depart[0]:
        depart.pop(0)
        trucks -= 1
    answer += (Fee[trucks-1]*trucks)

print(answer)
