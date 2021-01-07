'''from collections import deque


def solution(N, road, K):
    graph = [[0 for _ in range(N)] for _ in range(N)]
    visited = [0 for _ in range(N)]
    dist = [0 for _ in range(N)]
    for s, e, d in road:
        if not graph[s-1][e-1] or not graph[e-1][s-1]:
            graph[s-1][e-1] = d
            graph[e-1][s-1] = d
        else:
            graph[s-1][e-1] = min(graph[e-1][s-1], d)
            graph[s-1][e-1] = min(d, graph[s-1][e-1])

    queue = deque()
    queue.append(0)
    visited[0] = 1
    while queue:
        x = queue.popleft()
        for y in range(x, N):
            if graph[x][y]:
                if not dist[y]:
                    dist[y] = dist[x] + graph[x][y]
                else:
                    dist[y] = min(dist[y], dist[x] + graph[x][y])
                queue.append(y)
    return sum(True for i in dist if i <= K)'''

import sys



from collections import deque


def solution(N, road, K):
    dist = [sys.maxsize] * N
    dist[0] = 0
    queue = deque()
    queue.append(1)
    for i in range(len(road)):
        if road[i][0] > road[i][1]:
            road[i][0], road[i][1] = road[i][1], road[i][0]
    while queue:
        x = queue.popleft()
        for i in range(len(road)):
            if road[i][0] == x:
                queue.append(road[i][1])
                dist[road[i][1]-1] = min(dist[road[i][1]-1], dist[x-1] + road[i][2])
    #print(dist)
    return sum(True for i in dist if i <= K)


from collections import deque
import sys
def solution(N, road, K):
    graph = [[0 for _ in range(N)] for _ in range(N)]
    dist = [sys.maxsize for _ in range(N)]
    dist[0] = 0

    for s, e, d in road:
        if not graph[s-1][e-1] or not graph[e-1][s-1]:
            graph[s-1][e-1] = d
            graph[e-1][s-1] = d
        else:
            graph[s-1][e-1] = min(graph[e-1][s-1], d)
            graph[s-1][e-1] = min(d, graph[s-1][e-1])

    queue = deque()
    queue.append(0)
    while queue:
        x = queue.popleft()
        for y in range(x, N):
            if graph[x][y]:
                if dist[y] > dist[x] + graph[x][y]:
                    dist[y] = dist[x] + graph[x][y]
                    queue.append(y)
    return len([i for i in dist if i <= K])


N = 5
road = 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))