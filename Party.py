import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(N+1)]
MAX = sys.maxsize

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    adj_lst[start].append([cost, end])


def dijsktra(start):
    queue = []
    heapq.heappush(queue, [0, start])
    distance = [MAX for _ in range(N+1)]
    distance[start] = 0

    while queue:
        d, s = heapq.heappop(queue)
        if distance[s] < d:
            continue

        for cost, e in adj_lst[s]:
            new_cost = cost + d
            if new_cost < distance[e]:
                distance[e] = new_cost
                heapq.heappush(queue, [new_cost, e])

    #print(distance)
    return distance

result = []

for i in range(1, N+1):
    result.append(dijsktra(i)[X] + dijsktra(X)[i])

print(max(result))
