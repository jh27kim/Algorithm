import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[N]]
answer = 0


def check(lst):
    for l in lst:
        if l == 1:
            return True
    return False


while not check(dp[-1]):
    temp = []
    for i in range(len(dp[-1])):
        #print(dp[-1][i])
        temp.append(dp[-1][i] - 1)
        if dp[-1][i] % K == 0:
            temp.append(dp[-1][i] // K)
    dp.append(temp)
    answer += 1
print(answer)
