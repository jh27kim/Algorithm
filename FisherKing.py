import copy

R, C, M = map(int, input().split())
sharks = [[0 for _ in range(C+1)] for _ in range(R+1)]
directions = [[0 for _ in range(C+1)] for _ in range(R+1)]
speed = [[0 for _ in range(C+1)] for _ in range(R+1)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[r][c] = z
    directions[r][c] = d
    speed[r][c] = s
answer = 0
movement = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def catch(n):
    global answer
    for j in range(1, R+1):
        if sharks[j][n]:
            answer += sharks[j][n]
            sharks[j][n] = 0
            directions[j][n] = 0
            speed[j][n] = 0
            break


def move():
    global sharks, directions, speed
    nsharks = [[0 for _ in range(C+1)] for _ in range(R+1)]
    ndirections = [[0 for _ in range(C+1)] for _ in range(R+1)]
    nspeed = [[0 for _ in range(C+1)] for _ in range(R+1)]
    for x in range(1, R+1):
        for y in range(1, C+1):
            if sharks[x][y]:
                nx, ny = copy.deepcopy(x), copy.deepcopy(y)
                size, m, v = sharks[x][y], movement[directions[x][y]-1], speed[x][y]
                incx, incy = m[0], m[1]
                while v > 0:
                    nx, ny = nx + incx, ny + incy
                    if not(R+1 > nx >= 1 and C+1 > ny >= 1):
                        incx, incy = -incx, -incy
                    v -= 1
                if nsharks[nx][ny] < sharks[x][y]:
                    nsharks[nx][ny] = sharks[x][y]
                    ndirections[nx][ny] = directions[x][y]
                    nspeed[nx][ny] = speed[x][y]
                sharks[x][y], directions[x][y], speed[x][y] = 0, 0, 0

    sharks = nsharks
    directions = ndirections
    speed = nspeed


start = 0
while start < C:
    start += 1
    catch(start)
    move()
print(answer)
