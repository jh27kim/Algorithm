import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

numbers.sort()
c = Counter(numbers).most_common(2)

print(round((sum(numbers)/N)))
print(numbers[N//2])
if len(c) == 1:
    print(c[0][0])
else:
    print(c[1][0] if c[1][1] == c[0][1] else c[0][0])
print(numbers[-1] - numbers[0])
