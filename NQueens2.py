def move(location, visited, num, n):
    x, y = location
    visited[x][y] += num
    movement = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

    for i in range(n):
        for m in movement:
            nx, ny = x + m[0]*(i+1), y + m[1]*(i+1)
            if n > nx >= 0 and n > ny >= 0:
                visited[nx][ny] += num


def dfs(q, d, n):
    global answer
    x, y = q
    if d == n:
        answer += 1
    for i in range(x, n):
        if i != x: y = 0
        for j in range(y, n):
            if not visited[i][j]:
                move([i, j], visited, 1, n)
                #print(visited)
                dfs([i, j + 1], d+1, n)
                #print(visited)
                move([i, j], visited, -1, n)


def solution(n):
    global visited
    if n == 1:
        return 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                move([i, j], visited, 1, n)
                print(visited)
                dfs([i, j+1], 1, n)
                move([i, j], visited, -1, n)
                print(visited)
    return answer


answer = 0
n = 4
visited = [[0 for _ in range(n)] for _ in range(n)]
print(solution(n))