import sys

N = int(sys.stdin.readline())
scores = [int(sys.stdin.readline()) for _ in range(N)]
answer = 0

if N == 1:
    print(scores[0])
    exit()

for i in range(len(scores)-1, 0, -1):
    if scores[i] - scores[i-1] <= 0:
        answer += abs(scores[i] - scores[i - 1]) + 1
        scores[i-1] -= abs(scores[i] - scores[i-1]) + 1
print(answer)
#print(scores)
