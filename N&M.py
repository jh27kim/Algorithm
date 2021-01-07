import itertools
import sys

N, M = map(int, sys.stdin.readline().split())
lst = [i for i in range(1, N+1)]
answer = itertools.permutations(lst, M)

#print(list(answer))
for i in answer:
    print("".join(str(x)+" " for x in i))