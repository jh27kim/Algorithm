import sys

N, K = map(int, sys.stdin.readline().split())
value = [int(sys.stdin.readline()) for _ in range(N)]
answer = 0

for i in range(N-1, -1, -1):
    if value[i] > K:
        continue
    q, r = divmod(K, value[i])
    K = r
    answer += q
print(answer)
