def solution(m, n, puddles):
    route = [[0 for _ in range(m)] for _ in range(n)]
    route[0][0] = 1
    for p1, p2 in puddles:
        route[p2-1][p1-1] = -1
    for i in range(m-1):
        if route[0][i+1] == -1:
            break
        route[0][i+1] = route[0][i]
    for j in range(n-1):
        if route[j+1][0] == -1:
            break
        route[j+1][0] = route[j][0]
    for x in range(1, n):
        for y in range(1, m):
            if route[x][y] == -1:
                continue
            if route[x-1][y] == -1 and route[x][y-1] == -1:
                continue
            if route[x-1][y] == -1:
                route[x][y] = route[x][y-1]
            elif route[x][y-1] == -1:
                route[x][y] = route[x-1][y]
            else:
                route[x][y] = route[x-1][y] + route[x][y-1]
            #print(route)
    return route[-1][-1]


m, n = 2, 2
puddles = [[1,2]]
print(solution(m,n,puddles))