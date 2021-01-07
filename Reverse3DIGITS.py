import math


def solution(n):
    answer = 0
    three = 1
    d = []
    lst = [2, 1, 0]
    while three <= n:
        three = three * 3
    three = three // 3
    while three > 0:
        for l in lst:
            if n - three * l >= 0:
                n -= three * l
                three = three // 3
                d.append(l)
                break
    three = 1
    for i in range(len(d)):
        answer += d[i]*three
        three = three * 3
    return answer

print(solution(45))

three =1
n = 45
r = []
while True:
    a, rest = divmod(n, 3)
    print(n, a, rest)

    n = a
    r.append(rest)
    if a == 0:
        break

g= 0
for idx, ele in enumerate(reversed(r)):
    print(ele, idx)
    g += ele*(3**idx)
print(g)
