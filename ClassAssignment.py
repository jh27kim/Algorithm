import sys
import heapq

N = int(input())
classes = []

for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    classes.append([s, t])

queue = []
classes.sort()

for i in range(N):
    if len(queue) != 0 and queue[0] <= classes[i][0]:
        heapq.heappop(queue)
    heapq.heappush(queue, classes[i][1])

print(len(queue))
