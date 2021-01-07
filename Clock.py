import sys


N = int(sys.stdin.readline())
answer = 0

if N >= 3:
    answer += (1800 - pow(15, 2)) * N + 3600
else:
    answer += (1800 - pow(15, 2)) * (N + 1)
print(answer)

temp  = ""
answer = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            temp = str(h) + str(m) + str(s)
            if '3' in temp:
                answer += 1
print(answer)