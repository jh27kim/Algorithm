N, K, D = map(int, input().split())
order = [list(map(int, input().split())) for _ in range(K)]

left = 0
right = N


def isShort(last):
    cnt = 0
    for i in range(K):
        l = min(order[i][1], last)
        if l >= order[i][0]:
            cnt += ((l-order[i][0])//order[i][2]) + 1
    return cnt >= D


while left <= right:
    mid = (left + right) // 2
    if isShort(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1
print(result)
