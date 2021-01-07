'''def solution(dirs):
    x, y = 5, 5
    edge_X = [[0 for _ in range(10)] for _ in range(10)]
    edge_Y = [[0 for _ in range(10)] for _ in range(10)]

    for command in dirs:
        if command == 'U':
            if check(x-1, y) is True:
                prev_x, prev_y = x, y
                x -= 1
                edge_Y[min(x, prev_x)][min(y, prev_y)] = 1

        elif command == 'D':
            if check(x+1, y) is True:
                prev_x, prev_y = x, y
                x += 1
                edge_Y[min(x, prev_x)][min(y, prev_y)] = 1
        elif command == 'L':
            if check(x, y-1) is True:
                prev_x, prev_y = x, y
                y -= 1
                edge_X[min(x, prev_x)][min(y, prev_y)] = 1
        elif command == 'R':
            if check(x, y+1) is True:
                prev_x, prev_y = x, y
                y += 1
                edge_X[min(x, prev_x)][min(y, prev_y)] = 1
    return sum(sum(lst) for lst in edge_X) + sum(sum(lst) for lst in edge_Y)


def check(x, y):
    return False if x < 0 or x > 10 or y < 0 or y > 10 else True

dirs = "ULURRDLLU"
print(solution(dirs))
'''


def solution(dirs):
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    d = {"U": 0, "L": 1, "D": 2, "R": 3}

    visited = set()
    answer = 0
    x, y = 0, 0
    for dir in dirs:
        i = d[dir]
        nx, ny = x + dxs[i], y + dys[i]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if (x, y, nx, ny) not in visited:
            visited.add(x, y, nx, ny)
            visited.add(nx, ny, x, y)
            answer += 1
        x, y = nx, ny
    return answer

dirs = "UD"
print(solution(dirs))