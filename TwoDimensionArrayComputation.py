from collections import defaultdict

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
time = 0


def sorting(board):
    maximum_size = 0
    new_board = []

    for i in range(len(board)):
        occurences = defaultdict(int)
        for j in range(len(board[i])):
            if board[i][j] != 0:
                occurences[board[i][j]] += 1

        new_list = list(occurences.items())
        new_list.sort(key=lambda x:(x[1], x[0]))
        flat_list = []

        for sub_list in new_list:
            for item in sub_list:
                flat_list.append(item)

        if len(flat_list) > 100:
            flat_list = flat_list[:100]

        new_board.append(flat_list)
        maximum_size = max(len(flat_list), maximum_size)

    for lst in new_board:
        while len(lst) < maximum_size:
            lst.append(0)

    return new_board


while time <= 100:
    if R-1 < len(board) and C-1 < len(board[0]):
        if board[R-1][C-1] == K:
            print(time)
            exit()

    if len(board) >= len(board[0]):
        board = sorting(board)
    else:
        colboard = sorting(list(map(list, zip(*board))))
        board = list(map(list, zip(*colboard)))

    time += 1


print(-1)
