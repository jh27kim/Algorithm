import math
def solution(n, k):
    answer = []
    ppl = [i+1 for i in range(n)]
    k -= 1

    while n:
        idx = k // math.factorial(n - 1)
        if idx < 0:
            idx = 0
        person = ppl[idx]
        del ppl[idx]
        answer.append(person)
        k = k % math.factorial(n-1)
        n -= 1
    return answer


n = 4
k = 8
print(solution(n, k))
import itertools
ppl = [i+1 for i in range(n)]
print(list(itertools.permutations(ppl, n)))