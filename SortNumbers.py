'''
import sys

N = int(input())
numbers = [sys.stdin.readline() for _ in range(N)]
print(*sorted(numbers), sep="\n")

'''

'''
import heapq

s = []
while numbers:
    heapq.heappush(s, numbers.pop())
for n in s:
    sys.stdout.write(n)
'''

'''
import sys

N = int(sys.stdin.readline())
d = dict()
while N:
    n = int(sys.stdin.readline())
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
    N -= 1

for i in sorted(d.items()):
    for j in range(i[1]):
        print(i[0])
'''

'''
n = input()
numbers = [i for i in n]
numbers.sort(reverse=True)
print("".join(numbers))
'''

'''
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
numbers.sort(key = lambda x: (x[1], x[0]))
for n in numbers:
    print(n[0], n[1])
'''

'''
import sys

N = int(sys.stdin.readline())
words = list(set(input() for _ in range(N)))
words.sort(key = lambda x: (len(x), x))


for i in range(len(words)):
    print(words[i])
'''

import sys

N = int(sys.stdin.readline())
ppl = list(zip(list(input().split() for _ in range(N)), list(range(N))))
#print(ppl)
ppl.sort(key=lambda x: (int(x[0][0]), x[1]))

for p in ppl:
    print(p[0][0], p[0][1])
