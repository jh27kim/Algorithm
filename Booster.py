import math

N, Q = map(int, input().split())
checkpoint = [list(map(int, input().split())) for _ in range(N)]
query = [list(map(int, input().split())) for _ in range(Q)]
visited = [0 for _ in range(len(checkpoint))]


def boost(location, H):
    available_checkpoint = set()
    x, y = location
    for i in range(len(checkpoint)):
        nx, ny = checkpoint[i]
        if nx == x and ny == y:
            continue

        dx = abs(nx - x)
        dy = abs(ny - y)
        if nx == x or ny == y:
            available_checkpoint.add(i)
        elif dx <= H or dy <= H:
            available_checkpoint.add(i)
    #print(available_checkpoint)
    return available_checkpoint


def sol(A, B, X):
    global done

    current_checkpoint = checkpoint[A]
    next_checkpoint = boost(current_checkpoint, X)
    for ind in next_checkpoint:
        if checkpoint[ind] == checkpoint[B]:
            done = True
            return
        if not visited[ind]:
            visited[ind] = 1
            sol(ind, B, X)
            visited[ind] = 0


for A, B, X in query:
    done = False
    sol(A-1, B-1, X)
    if done:
        print('YES')
    else:
        print('NO')