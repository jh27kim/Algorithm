'''N = int(input())
population = list(map(int, input().split()))
graph = [[0 for _ in range(N)] for _ in range(N)]
answer = []
nodes = list(range(N))
visited = [0 for _ in range(N)]
queue = []
total = sum(population)


def sol():
    a = False
    temp1, temp2 = 0, 0
    queue2 = list(set(nodes) - set(queue))
    for n in queue:
        for x1 in range(n+1, N):
            if graph[n][x1] and x1 in queue:
                temp1 += 1
    for n1 in queue2:
        for x2 in range(n1+1, N):
            if graph[n1][x2] and x2 in queue2:
                temp2 += 1
    if temp1 >= len(queue)-1 and temp2 >= len(queue2)-1:
        a = True
    #print(queue, a)
    #print(temp1, temp2)
    return a


def dfs(x, level):
    if depth == level:
        result = 0
        if sol():
            for item in queue:
                result += population[item]
            #print(queue, result)
            answer.append(abs(result-(total-result)))
        return
    for n in range(x, len(visited)):
        if not visited[n]:
            queue.append(nodes[n])
            visited[n] = 1
            dfs(n+1, level+1)
            visited[n] = 0
            queue.pop()


for i in range(N):
    node = list(map(int, input().split()))
    for j in range(1, len(node)):
        graph[i][node[j]-1] = 1

for d in range(N//2):
    depth = d+1
    dfs(0, 0)

if not answer:
    print(-1)
else:
    #print(answer)
    print(min(answer))
'''


from collections import deque
import sys

input = sys.stdin.readline

def bfs(g):
    q = deque()
    check = [0 for _ in range(n)]
    q.append(g[0])
    check[g[0]] = 1
    cnt, ans = 1, 0
    while q:
        x = q.popleft()
        ans += people[x]
        for nx in a[x]:
            if nx in g and not check[nx]:
                check[nx] = 1
                cnt += 1
                q.append(nx)
    if cnt == len(g):
        return ans
    else:
        return 0

def dfs(cnt, x, end):
    global min_ans
    if cnt == end:
        g1, g2 = deque(), deque()
        for i in range(n):
            if c[i]:
                g1.append(i)
            else:
                g2.append(i)
        ans1 = bfs(g1)
        if not ans1:
            return
        ans2 = bfs(g2)
        if not ans2:
            return
        min_ans = min(min_ans, abs(ans2 - ans1))
        return

    for i in range(x, n):
        if c[i]:
            continue
        c[i] = 1
        dfs(cnt+1, i, end)
        c[i] = 0

n = int(input())
people = list(map(int, input().split()))

a = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(1, x[0]+1):
        a[i].append(x[j]-1)
#print(a)
min_ans = sys.maxsize
for i in range(1, n // 2 + 1):
    c = [0 for _ in range(n)]
    dfs(0, 0, i)

if min_ans == sys.maxsize:
    print(-1)
else:
    print(min_ans)