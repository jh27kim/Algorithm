N, L = map(int, input().split())
leaks = list(map(int, input().split()))

leaks.sort()
start = leaks[0]
answer = 1

for i in range(1, len(leaks)):
    #print(start, answer)
    if leaks[i] - start + 1 <= L:
        #print('con')
        continue
    start = leaks[i]
    answer += 1

print(answer)
