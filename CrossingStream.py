def check(stones, ind, k):
    res = 0
    while stones[ind] == 0:
        res += 1
        ind += 1
        if ind == len(stones):
            break
    return True if res >= k else False


def solution(stones, k):
    answer = 0
    while True:
        for i in range(len(stones)):
            if stones[i] == 0:
                if check(stones, i, k):
                    return answer
                continue
            stones[i] -= 1
        answer += 1
    return answer


def sol(stones, k, mid):
    num = 0
    for stone in stones:
        if stone < mid:
            num += 1
        else:
            num = 0
        if num >= k:
            return False
    return True


def solution(stones, k):
    left = 1
    right = max(stones) + 1
    while left < right - 1:
        mid = (left + right) // 2
        if sol(stones, k, mid):
            left = mid
        else:
            right = mid
    return left


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))