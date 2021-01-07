from collections import deque


def can_move(cur1, cur2, new_board):
    movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    rotation = [1, -1]
    cand = []

    for m in movement:
        nx1 = (cur1[0]+m[0], cur1[1]+m[1])
        nx2 = (cur2[0]+m[0], cur2[1]+m[1])
        if new_board[nx1[0]][nx1[1]] + new_board[nx2[0]][nx2[1]] == 0:
            cand.append((nx1, nx2))

    if cur1[0] == cur2[0]:
        for m in rotation:
            if new_board[cur1[0]+m][cur1[1]] + new_board[cur2[0]+m][cur2[1]] == 0:
                cand.append((cur1, (cur1[0]+m, cur1[1])))
                cand.append((cur2, (cur2[0]+m, cur2[1])))
    else:
        for m in rotation:
            if new_board[cur1[0]][cur1[1]+m] + new_board[cur2[0]][cur2[1]+m] == 0:
                cand.append((cur1, (cur1[0], cur1[1]+m)))
                cand.append((cur2, (cur2[0], cur2[1]+m)))
    return cand


def solution(board):
    N = len(board)
    new_board = [[1 for _ in range(N+2)] for _ in range(N+2)]
    GOAL = (N, N)
    for x in range(N):
        for y in range(N):
            new_board[x+1][y+1] = board[x][y]

    queue = deque([((1, 1), (1, 2), 0)])
    visited = set(((1, 1), (1, 2)))

    while queue:
        cur1, cur2, count = queue.popleft()
        if cur1 == GOAL or cur2 == GOAL:
            return count
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in visited:
                queue.append((*nxt, count+1))
                visited.add(nxt)


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
