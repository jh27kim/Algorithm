import sys

N = int(sys.stdin.readline())
parts = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
requested = list(map(int, sys.stdin.readline().split()))

parts.sort()

def binary_search(lst, target):
    start, end = 0, len(lst)-1

    while start <= end:
        mid = (start + end)//2
        if lst[mid] == target:
            return True
        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


for p in requested:
    if binary_search(parts, p):
        print("yes")
        continue
    print("no")

