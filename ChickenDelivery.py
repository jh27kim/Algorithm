import sys
from collections import deque
from itertools import combinations


def find_distance(stores):
    distances = []
    for x in range(N):
        for y in range(N):
            if city[x][y] == 1:
                d = sys.maxsize
                for n, m in stores:
                    d = min(d, abs(x-n) + abs(y-m))
                distances.append(d)
    return sum(distances)


def dfs(queue):
    global answer
    if len(queue) == M:
        answer = min(answer, find_distance(queue))

    for i in range(N):
        for j in range(N):
            if city[i][j] == 2 and not visited[i][j]:
                visited[i][j] = 1
                queue.append([i, j])
                dfs(queue)
                visited[i][j] = 0
                queue.pop()


answer = sys.maxsize
N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

dfs(queue)

lst = [1,23,5,4,2,775,24,33,55]
import bisect
bisect.bisect()
print(answer)
