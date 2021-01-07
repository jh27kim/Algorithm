from collections import deque

V, E = map(int, input().split())
graph = [[] for _ in range(V)]
queue = deque()
answer = []
rank = [0 for _ in range(V)]

for i in range(E):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    rank[b-1] += 1
    print(a, b, rank)


def insert(graph):
    global answer
    for i in range(V):
        if rank[i] == 0:
            queue.append(i)
            answer.append(i+1)
    return queue


queue = insert(graph)
print(queue)

while queue:
    lenq = len(queue)
    while lenq:
        x = queue.pop()
        rank[x] -= 1
        for i in range(len(graph[x])):
            rank[graph[x][i]] -= 1
        print(rank)
        lenq -= 1
    insert(graph)

print(answer)

