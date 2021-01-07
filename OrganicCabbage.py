T = int(input())
coordinates = []
inc = [[1,0], [-1,0], [0,1], [0,-1]]

for i in range(T):
    M, N, K = map(int, input().split())
    for j in range(K):
        coordinates.append(list(map(int, input().split())))

    visited = []
    answer = 0
    while coordinates:
        start = coordinates.pop()
        visited = [start]
        queue = [start]
        while queue:
            for dx, dy in inc:
                if [start[0]+dx, start[1]+dy] in coordinates and [start[0]+dx, start[1]+dy] not in visited:
                    visited.append([start[0]+dx, start[1]+dy])
                    queue.append([start[0]+dx, start[1]+dy])
                    coordinates.remove([start[0]+dx, start[1]+dy])
            start = queue.pop()
        answer += 1
    print(answer)
