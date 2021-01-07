import math

cases = int(input())
looks = dict()
answer = []
for i in range(cases):
    n = int(input())
    for j in range(n):
        cloth, gear = input().split()
        if gear in looks:
            looks[gear] += 1
        else:
            looks[gear] = 2
    answer.append(math.prod(looks.values()))
    looks = dict()

for k in answer:
    print(k-1)