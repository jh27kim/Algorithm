import sys
import heapq

N = int(input())
ramen = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ramen.sort()
queue = []

day = 0
answer = 0
print(ramen)

for i in range(len(ramen)):
    heapq.heappush(queue, ramen[i][1])
    if i[0] < len(queue):
        heapq.heappop()

print(answer)
