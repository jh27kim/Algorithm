def gcd(n, m):
    return m if n%m == 0 else gcd(m, n%m)


def solution(arr):
    queue = []
    while arr:
        queue.append(arr.pop())
        if len(queue) == 2:
            M, m = max(queue), min(queue)
            arr.append(M*m // gcd(M, m))
            queue = []
    return queue[-1]

arr = [12, 18, 21]
print(solution(arr))
