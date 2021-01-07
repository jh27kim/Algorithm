from collections import deque
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k = list(map(int, input().split()))
nut = [list(map(int, input().split())) for _ in range(n)]
board = [[5]*n for _ in range(n)]
trees_dict = {(i,j): deque() for i in range(n) for j in range(n)}

for _ in range(m):
    x, y, age = list(map(int, input().split()))
    trees_dict[(x-1, y-1)].append(age)

year = 0

while True:
    added_nut = [[0]*n for _ in range(n)]
    for (x, y), trees in trees_dict.items():
        survived_trees = deque()
        for tree in trees:
            if board[x][y] >= tree:
                survived_trees.append(tree+1)
                board[x][y] -= tree
            else:
                added_nut[x][y] += tree // 2
        trees_dict[(x, y)] = survived_trees

    for (x, y), trees in trees_dict.items():
        board[x][y] += added_nut[x][y]

    new_trees = {(i,j): 0 for i in range(n) for j in range(n)}
    for (x, y), trees in trees_dict.items():
        for tree in trees:
            if tree % 5 == 0:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        new_trees[(nx, ny)] += 1
    for (x, y), size in new_trees.items():
        for _ in range(size):
            trees_dict[(x, y)].appendleft(1)

    for i in range(n):
        for j in range(n):
            board[i][j] += nut[i][j]
    year += 1
    if year == k:
        answer = 0
        for (x, y), trees in trees_dict.items():
            answer += len(trees)
        print(answer)
        break

