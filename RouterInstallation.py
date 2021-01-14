import sys

N, C = map(int, input().split())
x = [int(sys.stdin.readline()) for _ in range(N)]
x.sort()
answer = 0


def check(mid):
    cnt = C-1
    prev = x[0]
    #print(x, mid)
    for i in range(1, len(x)):
        if x[i] - prev < mid:
            continue
        #print(x[i])
        cnt -= 1
        prev = x[i]
    return True if cnt <= 0 else False


left, right = 1, x[-1]

while left <= right:
    mid = (left + right)//2
    if check(mid):
        #print(mid)
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)