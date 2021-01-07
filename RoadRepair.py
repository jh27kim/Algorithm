from sys import stdin

input = stdin.readline
N, L = map(int, input().split())
p = [[int(x) for x in input().split()] for i in range(N)]
p.sort()
res, s = 0, 0

for i in range(N):
    s = max(p[i][0], s)
    diff = p[i][1] - s
    count = (diff + L - 1) // L
    res += count
    s += count * L

print(res)
