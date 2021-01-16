import bisect

N, x = map(int, input().split())
lst = list(map(int, input().split()))

lower_bound = bisect.bisect_left(lst, x)
upper_bound = bisect.bisect_right(lst, x)

answer = upper_bound - lower_bound
if not answer:
    print(-1)
else:
    print(answer)


def first(a, b, arr, target):
    if a > b:
        return None
    mid = (a+b)//2
    if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return first(mid+1, b, arr, target)
    else:
        return first(a, mid-1, arr, target)


def last(a, b, arr, target):
    if a > b:
        return None
    mid = (a+b)//2
    if (mid == N-1 or arr[mid+1] > target) and arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return first(mid+1, b, arr, target)
    else:
        return first(a, mid-1, arr, target)