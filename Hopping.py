cache = {}
def fib(n):
    if n not in cache.keys():
        cache[n] = solution(n)
    return cache[n]

def solution(n):
    if n <= 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = 4
print(solution(n))