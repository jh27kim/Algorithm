import sys

MAX = sys.maxsize
N, M, K, X = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
distances = [0 for _ in range(N+1)]
answer = []


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a].append(b)

'''
def dijsktra(start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        dist, A = heapq.heappop(queue)
        if distances[A] < dist:
            continue
        for B in adj_lst[A]:
            cost = dist + 1
            if cost < distances[B]:
                distances[B] = cost
                heapq.heappush(queue, [cost, B])


dijsktra(X)
for i in range(N+1):
    if distances[i] == K:
        answer.append(i)
if answer:
    print(*answer, sep="\n")
else:
    print(-1)
    '''


from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    distances[start] = 0

    cnt = 0

    while queue:
        lenq = len(queue)

        while lenq:
            x = queue.popleft()
            #print(x, adj_lst)
            for y in adj_lst[x]:
                if distances[y] == 0:
                    queue.append(y)
                    distances[y] = distances[x] + 1
            lenq -= 1

        cnt += 1
        if cnt == K:
            return distances

distances = bfs(X)
answer = []

for i in range(N+1):
    if distances[i] == K:
        answer.append(i)
if answer:
    print(*answer, sep="\n")
else:
    print(-1)
