import sys

N, M = map(int, sys.stdin.readline().split())
occupied = [[False for _ in range(N+1)] for _ in range(N+1)]
answer = 0

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    occupied[x][y], occupied[y][x] = True, True

'''
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if occupied[i][j]:
            continue
        for k in range(j+1, N+1):
            if occupied[i][k] or occupied[j][k]:
                continue
            answer += 1
print(answer)
'''

queue = []

def check(queue):
    global answer
    x, y, z = queue
    #print(queue)
    if occupied[x][y] or occupied[y][z] or occupied[z][x]:
        return
    #print(queue)
    answer += 1


def dfs(depth, x):
    if depth == 3:
        check(queue)
        return
    for i in range(x+1, N+1):
        queue.append(i)
        dfs(depth+1, i)
        queue.pop()


dfs(0, 0)
print(answer)
