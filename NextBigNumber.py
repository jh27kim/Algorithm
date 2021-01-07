def convert(m):
    two = []
    while True:
        q, r = divmod(m, 2)
        m = q
        two.append(r)
        if q == 0:
            break
    return sum(two)


def solution(n):
    a = convert(n)
    for i in range(n+1,1000001):
        if convert(i) == a:
            return i


n = 78
print(solution(n))