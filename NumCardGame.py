import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

for row in range(N):
    answer = max(answer, min(board[row]))

print(answer)