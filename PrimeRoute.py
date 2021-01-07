from collections import deque
import math

T = int(input())


def digitcheck(a, b):
    tolerance = False
    a, b = list(str(a)), list(str(b))
    for i in range(len(a)):
        if a[i] != b[i]:
            if tolerance:
                return False
            tolerance = True
    return True


def primecheck(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def BFS(q):
    cnt = 0
    visited.append(q[-1])
    while q:
        lenq = len(q)
        while lenq:
            x = q.popleft()
            for j in range(1000, 10000):
                if digitcheck(x, j):
                    if primecheck(j) and j not in visited:
                        if j == end:
                            return cnt + 1
                        q.append(j)
                        visited.append(j)

            lenq -= 1
        cnt += 1
    return "Impossible"


for i in range(T):
    start, end = map(int, input().split())
    visited = []
    queue = deque()
    queue.append(start)
    if start == end:
        print(0)
    else:
        print(BFS(queue))

