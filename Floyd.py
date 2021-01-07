import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
MAX = sys.maxsize

graph = [[] for _ in range(N+1)]
distance = [[MAX if n != m else 0 for n in range(N+1)] for m in range(N+1)]

for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    if cost < distance[x][y]:
        distance[x][y] = cost

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):

            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])
            print(distance[2][1], k, a, b)

for x in range(1, N+1):
    for y in range(1, N+1):
        if distance[x][y] == MAX:
            print(0, end=" ")
            continue
        print(distance[x][y], end=" ")
    print('\n')
