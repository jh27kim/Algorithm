import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
MAX = sys.maxsize

graph = [[] for _ in range(N+1)]
costs = [MAX for _ in range(N+1)]

for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph[x].append((y, cost))


def dijksra(start):
    q = []
    heapq.heappush(q, (0, start))
    costs[start] = 0

    while q:
        value, node = heapq.heappop(q)
        if value > costs[node]:
            continue
        for i in graph[node]:
            cost = value + i[1]
            if cost < costs[i[0]]:
                costs[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijksra(start)
print(costs)
