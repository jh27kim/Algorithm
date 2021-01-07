import copy
def solution(board):
    answer = 0
    loc = [[[1, 1], [1, 2]]]
    finish = [len(board), len(board)]
    visited = [[[1,1], [1,2]]]

    while True:
        answer += 1
        loc = DFS(loc.pop(0), visited)
        for i in loc:
            if finish in i:
                return answer

def DFS(coordinates, visited):
    a1 = copy.deepcopy(coordinates)
    a2 = copy.deepcopy(coordinates)
    a3 = copy.deepcopy(coordinates)
    a4 = copy.deepcopy(coordinates)
    a5 = copy.deepcopy(coordinates)
    a6 = copy.deepcopy(coordinates)

    move = []
    if error(a1, 'MR'):
        if a1 not in visited:
            move.append(a1)
            visited.append(a1)
    if error(a2, 'ML'):
        if a2 not in visited:
            move.append(a2)
            visited.append(a2)
    if error(a3, 'BA'):
        if a3 not in visited:
            move.append(a3)
            visited.append(a3)
    if error(a4, 'BC'):
        if a4 not in visited:
            move.append(a4)
            visited.append(a4)
    if error(a5, 'FA'):
        if a5 not in visited:
            move.append(a5)
            visited.append(a5)
    if error(a6, 'FC'):
        if a6 not in visited:
            move.append(a6)
            visited.append(a6)
    return move


def moveRight(pos):
    pos[0][1] += 1
    pos[1][1] += 1
    return pos

def moveLeft(pos):
    pos[0][1] -= 1
    pos[1][1] -= 1
    return pos


##뒤에꺼 기준
def BackAntiClockwise(pos):
    pos[0][0] += 1
    pos[0][1] += 1
    return pos

##앞에꺼 기준
def BackClockwise(pos):
    pos[0][0] -= 1
    pos[0][1] += 1
    return pos


def FrontClockwise(pos):
    pos[1][0] += 1
    pos[1][1] -= 1
    return pos


def FrontAntiClockwise(pos):
    pos[1][0] -= 1
    pos[1][1] -= 1
    return pos

def error(pos, key):
    if key == 'MR':
        pos = moveRight(pos)
    elif key == 'ML':
        pos = moveLeft(pos)
    elif key == 'BA':
        pos = BackAntiClockwise(pos)
    elif key == 'BC':
        pos = BackClockwise(pos)
    elif key == 'FC':
        pos = FrontClockwise(pos)
    elif key == 'FA':
        pos = FrontAntiClockwise(pos)

    x1, y1 = pos[0][0], pos[0][1]
    x2, y2 = pos[1][0], pos[1][1]
    if x1 > len(board) or x2 > len(board) or y1 > len(board) or y2 > len(board):
        return False
    elif board[x1-1][y1-1] == 1 or board[x2-1][y2-1] == 1:
        return False
    elif x1*x2*y1*y2 <= 0:
        return False
    else:
        return True

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))

