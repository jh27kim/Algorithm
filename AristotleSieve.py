import sys
import math

N = int(sys.stdin.readline().rstrip())
sieve = [True for _ in range(N+1)]

for i in range(2, int(math.sqrt(N))+1):
    if sieve[i]:
        j = 2
        while i*j < N:
            sieve[i*j] = False
            j += 1

print(sieve)
