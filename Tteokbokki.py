import sys

N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))


def check(lst, target, height):
    ans = 0
    for i in range(len(lst)):
        if lst[i] <= height:
            continue
        ans += lst[i] - height
    return ans > target


start, end = 0, max(heights)
while start <= end:
    mid = (start + end)//2
    if check(heights, M, mid):
        start = mid + 1
    else:
        end = mid - 1

print(start)
