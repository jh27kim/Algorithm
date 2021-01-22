import math

N, M = map(int, input().split())
balls = list(map(int, input().split()))
lst = [0] * (M+1)

total = math.factorial(N)/(2*math.factorial(N-2))

for i in balls:
    lst[i] += 1

for j in lst:
    if j >= 2:
        total -= math.factorial(j)/(2*math.factorial(j-2))

print(int(total))
