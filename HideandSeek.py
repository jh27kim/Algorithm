import heapq
import sys

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
MAX = sys.maxsize
distances = [MAX for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adj_lst[A].append(B)
    adj_lst[B].append(A)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, [0, start])
    distances[start] = 0

    while queue:
        dist, X = heapq.heappop(queue)
        if dist > distances[X]:
            continue

        for Y in adj_lst[X]:
            cost = distances[X] + 1
            if distances[Y] > cost:
                distances[Y] = cost
                heapq.heappush(queue, [cost, Y])


dijkstra(1)
M = -MAX
ind = 0
answer = 0

for i in range(1, N+1):
    if distances[i] > M:
        M = distances[i]
        ind = i
        answer = 0
    if distances[i] == M:
        answer += 1

print(ind, M, answer)
