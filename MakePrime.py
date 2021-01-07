def dfs(q, d, x, nums, sieve):
    global answer
    if len(q) == 3 and sieve[sum(q)]:
        answer += 1
        return
    for i in range(x, len(nums)):
        q.append(nums[i])
        # print(q, x)
        dfs(q, d + 1, i + 1, nums, sieve)
        q.pop()
        # print(q, x)


from collections import deque
import math


def solution(nums):
    global answer
    answer = 0
    m = max(nums) * 3
    sieve = [1 for _ in range(m)]
    length = math.ceil(m ** 0.5)
    sieve[1] = 0
    sieve[0] = 0

    for i in range(2, length):
        if sieve[i]:
            for j in range(2 * i, m, i):
                sieve[j] = 0

    queue = deque()
    dfs(queue, 0, 0, nums, sieve)
    return answer