'''
import copy

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
movement = [[-1, 0], [0, -1], [1, 0], [0, 1]]
built = [[0 for _ in range(N)] for _ in range(N)]
answer = 0


def check(board):
    res = 0
    #print(np.asarray(board))

    for i in range(N):
        road = board[i]
        if len(set(road)) == 1:
            res += 1

        road = [board[r][i] for r in range(N)]
        if len(set(road)) == 1:
            res += 1

    return res


def dfs(visited):
    global answer
    answer = max(answer, check(board))

    visited = copy.deepcopy(visited)

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                visited[x][y] = 1
                for m in movement:
                    nx, ny = x, y
                    queue = [[x, y]]

                    for l in range(L-1):
                        nx += m[0]
                        ny += m[1]
                        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == board[x][y]:
                            queue.append([nx, ny])

                    if len(queue) == L:
                        avail = True
                        for x1, y1 in queue:
                            if built[x1][y1]:
                                avail = False
                                break

                        if avail:
                            for x1, y1 in queue:
                                board[x1][y1] += 1
                                built[x1][y1] = 1

                            #print(x, y, m)
                            dfs(visited)
                            #print(x, y, m)

                            for x1, y1 in queue:
                                board[x1][y1] -= 1
                                built[x1][y1] = 0


dfs(visited)
print(answer)
'''


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def solve(N, L, board):
    zip_board = list(map(list, list(zip(*board))))
    c1 = counting(N, L, board)
    c2 = counting(N, L, zip_board)
    return c1 + c2


def counting(N, L, board):
    res = 0
    for i in range(N):
        prev = board[i][0]
        cnt = 1
        for j in range(1, N):
            if board[i][j] == prev:
                cnt += 1
                prev = board[i][j]
                continue

            elif board[i][j] == prev + 1:
                if cnt >= L:
                    cnt = 1
                    prev = board[i][j]
                else:
                    break

            elif board[i][j] == prev - 1 and cnt >= 0:
                cnt = 1 - L
                prev = board[i][j]
            else:
                break

        else:
            if cnt >= 0:
                res += 1

    return res


print(solve(N, L, board))
