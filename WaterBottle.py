from collections import deque
import itertools
import copy

A, B, C = map(int, input().split())
queue, answer, visited = deque(), [], []
queue.append([0, 0, C])
vol = [A, B, C]
ways = list(itertools.permutations([0, 1, 2], 2))


def bfs():
    while queue:
        v = queue.popleft()
        if v[0] == 0 and v[2] not in answer:
            answer.append(v[2])
        for i in range(len(ways)):
            temp = copy.deepcopy(v)
            start, end = ways[i]
            if temp[end] + temp[start] > vol[end]:
                temp[start] = v[end] + v[start] - vol[end]
                temp[end] = vol[end]
            else:
                temp[start] = 0
                temp[end] += v[start]
            if temp not in visited:
                visited.append(temp)
                queue.append(temp)


bfs()
answer.sort()
print(*answer, sep=" ")

