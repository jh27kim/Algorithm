def solution(n):
    sieve = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        sieve -= set(range(2*i, n+1, i))
    return len(sieve)


n = 100
print(solution(n))