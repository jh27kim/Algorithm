import sys
import heapq

N, M, C = map(int, sys.stdin.readline().split())
MAX = sys.maxsize
distance = [MAX for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))

start = C
distance[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    value, node = heapq.heappop(q)
    if distance[node] < value:
        continue

    for i in graph[node]:
        cost = value + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt = 0
time = 0
for i in range(1, N+1):
    if distance[i] != MAX:
        cnt += 1
        time = max(time, distance[i])
print(distance)
print(cnt-1, time)