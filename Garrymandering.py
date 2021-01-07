import itertools
import sys
from collections import deque


def check(q1):
    #print(q1)
    visited = [0 for _ in range(N)]
    queue = deque()
    queue.append(q1[0])
    visited[q1[0]] = 1

    while queue:
        x = queue.pop()
        for i in range(N):
            if board[x][i] and not visited[i] and i in q1:
                queue.append(i)
                visited[i] = 1

    for k in q1:
        if not visited[k]:
            return False
    return True


answer = sys.maxsize
N = int(input())
population = list(map(int, input().split()))
board = [[0 for _ in range(N)] for _ in range(N)]
total = sum(population)

for i in range(N):
    cities = list(map(int, input().split()))
    for j in range(1, len(cities)):
        board[i][cities[j]-1], board[cities[j]-1][i] = 1, 1

lst = list(range(N))
for c in range(1, N//2 + 1):
    comb = list(itertools.combinations(lst, c))
    for x in comb:
        if check(list(x)) and check(list(set(lst) - set(x))):
            a = sum([population[y] for y in x])
            b = total - a
            answer = min(answer, abs(a-b))

if N == 2:
    for x1 in range(N):
        for y1 in range(N):
            if board[x1][y1] == 1:
                print(-1)
                exit()
    print(answer)
else:
    print(-1 if answer > total-min(population) else answer)
