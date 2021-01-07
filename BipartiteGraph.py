'''import itertools


def check(lst):
    A, B = set(), set()
    for n in nodes:
        if n in c:
            for k in range(V):
                if board[n-1][k]:
                    A.add(k+1)
        else:
            for k in range(V):
                if board[n-1][k]:
                    B.add(k+1)
    return True if len(A) + len(B) == V else False


K = int(input())

while K:
    V, E = map(int, input().split())
    lines = [list(map(int, input().split())) for _ in range(E)]
    nodes = list(range(1, V+1))
    board = [[0 for _ in range(V)] for _ in range(V)]
    for x, y in lines:
        board[x-1][y-1] = 1
        board[y-1][x-1] = 1

    done = False
    for i in range(1, (V//2) + 1):
        comb = list(itertools.combinations(nodes, i))
        for c in comb:
            done = check(c)
            if done:
                break
        if done:
            break
    if done:
        print("YES")
    else:
        print("NO")
    K -= 1
'''
import sys


def bfs(v, visited, color):
    q = [v]
    visited[v] = True
    color[v] = 1

    while q:
        x = q.pop()
        for nx in adj_lst[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
                color[nx] = 3 - color[x]
            else:
                if color[x] == color[nx]:
                    return False
    return True


for tc in range(int(sys.stdin.readline())):
    V, E = map(int, sys.stdin.readline().split())
    adj_lst = [[] for _ in range(V+1)]
    visited = [False for _ in range(V + 1)]
    color = [0 for _ in range(V + 1)]
    flag = True

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        adj_lst[a].append(b)
        adj_lst[b].append(a)

    for node in range(1, V+1):
        if not visited[node]:
            if not bfs(node, visited, color):
                flag = False
                break

    if flag == False:
        print("NO")
    else:
        print("YES")
