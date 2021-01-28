import sys

N, C = map(int, input().split())
x = list(int(sys.stdin.readline()) for _ in range(N))

x.sort()
left, right = 1, x[-1]
answer = 0

while left <= right:
    mid = (left + right) // 2
    routers = 1
    start = x[0]
    for i in range(1, len(x)):
        nxt = start + mid
        #print(nxt, mid)
        if x[i] < nxt:
            continue
        start = x[i]
        routers += 1
    #print(routers, mid)

    if routers >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
