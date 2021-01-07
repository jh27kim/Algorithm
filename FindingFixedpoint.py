import sys

N = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split()))
left, right = 0, N-1
answer = -1

while left <= right:
    mid = (left+right)//2
    print(left, mid, right)
    if points[mid] > mid:
        right = mid - 1
    else:
        if points[mid] == mid:
            answer = mid
            break
        left = mid + 1

print(answer)