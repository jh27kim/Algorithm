import sys

K, N = map(int, sys.stdin.readline().split())
lanes = [int(sys.stdin.readline().replace("\n", "")) for _ in range(K)]

left = 1
right = max(lanes)
answer = 0

while left <= right:
    mid = (left + right) // 2

    if N <= sum(x // mid for x in lanes):
        left = mid + 1
    else:
        right = mid - 1
print(right)

