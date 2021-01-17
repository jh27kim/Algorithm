N = int(input())
fear = list(map(int, input().split()))

fear.sort()
start = fear[0]
cnt = 1
answer = 0

for i in range(1, len(fear)):
    if start == fear[i]:
        cnt += 1
    else:
        if cnt >= start:
            answer += 1
        start = fear[i]
        cnt = 0
if cnt >= start:
    print(answer + 1)
else:
    print(answer)
