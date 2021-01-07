import sys

X = int(sys.stdin.readline())
answer = sys.maxsize


def dfs(x, d):
    global answer
    if x <= 0:
        return
    if x == 1:
        answer = min(answer, d)
        return
    if x % 5 == 0:
        dfs(x//5, d+1)
    if x % 3 == 0:
        dfs(x//3, d+1)
    if x % 2 == 0:
        dfs(x//2, d+1)
    dfs(x-1, d+1)


dfs(X, 0)
print(answer)

dp = set()
dp.add(X)
cnt = 0

while 1 not in dp:
    temp = set()
    for i in dp:
        if i % 5 == 0:
            temp.add(i//5)
        if i % 3 == 0:
            temp.add(i//3)
        if i % 2 == 0:
            temp.add(i//2)
        if i-1 > 0:
            temp.add(i-1)
    dp = set()
    dp = temp
    print(dp)
    cnt += 1
print(cnt)