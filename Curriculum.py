import sys
from collections import deque
import copy

'''
N = int(sys.stdin.readline())
indegree = [0 for _ in range(N+1)]
costs = [0 for _ in range(N+1)]
lectures = [[] for _ in range(N+1)]
queue = deque()


def receive_input(*arg, n):
    arg = arg[0]
    costs[n] = arg[0]
    if len(arg) >= 2:
        for i in range(1, len(arg)):
            lectures[arg[i]].append(n)
            indegree[n] += 1
    else:
        queue.append(n)


for n in range(1, N+1):
    inst = list(map(int, sys.stdin.readline().split()))
    receive_input(inst[:-1], n=n)

result = copy.deepcopy(costs)

while queue:
    x = queue.popleft()

    for i in lectures[x]:
        indegree[i] -= 1
        result[i] = max(result[i], costs[i] + result[x])
        if indegree[i] == 0:
            queue.append(i)

print(result)
'''

import random
print(random.randint(1,48))