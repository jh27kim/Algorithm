import sys

S, C = map(int, sys.stdin.readline().split())
L = [int(input()) for _ in range(S)]
left, right = 1, max(L)


def check(length):
    availableChicken = 0
    for i in range(len(L)):
        availableChicken += L[i] // length
        if availableChicken >= C:
            return True
    return False


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        ret = mid
    else:
        right = mid - 1
print(sum(L) - ret*C)
