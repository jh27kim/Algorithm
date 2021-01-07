import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
cnt = 0
ind = 0

arr.sort(reverse=True)

answer += ((M//(K+1)) * K + (M%(K+1))) * arr[0]
print(answer)
answer += (M//(K+1)) * arr[1]
print(answer)
