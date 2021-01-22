import sys

A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())
robot_status = []
board = [[0 for _ in range(A)] for _ in range(B)]

for i in range(N):
    x, y, d = sys.stdin.readline().split()
    board[B-int(y)][int(x)-1] = i+1
    robot_status.append([int(x), int(y), d])

instructions = []
for i in range(M):
    r, i, repeat = sys.stdin.readline().split()
    instructions.append([int(r), i, int(repeat)])
#import numpy as np
DIRECTION = {'N': [1, 0], 'W': [0, -1], 'S': [-1, 0], 'E': [0, 1]}
LEFT_ROTATION = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
RIGHT_ROTATION = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

#print(np.asarray(board))

for inst in instructions:
    robot, move, repeat = inst
    x, y, d = robot_status[robot-1]

    if move == 'F':
        dy, dx = DIRECTION[d]
        board[B-y][x-1] = 0
        for i in range(repeat):
            x += dx
            y += dy
            #print(board)
            if B-y < 0 or B-y >= B or x-1 < 0 or x-1 >= A:
                print("Robot " + str(robot) + " crashes into the wall")
                exit()

            if board[B-y][x-1]:
                print("Robot " + str(robot) + " crashes into robot " + str(board[B-y][x-1]))
                exit()

        robot_status[robot-1][0] = x
        robot_status[robot-1][1] = y
        board[B-y][x-1] = robot

    elif move == 'L':
        nd = d
        for i in range(repeat):
            nd = LEFT_ROTATION[nd]
        robot_status[robot - 1][2] = nd

    elif move == 'R':
        nd = d
        for i in range(repeat):
            nd = RIGHT_ROTATION[nd]
        robot_status[robot - 1][2] = nd

    #print(np.asarray(board))
print('OK')

'''
5 3
2 4
2 2 E
4 3 W
2 F 1
1 F 1
2 R 1
2 F 1
'''