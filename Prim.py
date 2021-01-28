import heapq

myedges = [
    (1, 0, 1), (2, 1, 2), (3, 0, 2)
]


def prim(start, edges):
    N = 3
    adjacent_edges = [[] for _ in range(N)]
    connected_nodes = set([start])
    mst = []

    for edge in edges:
        cost, X, Y = edge
        adjacent_edges[X].append([cost, X, Y])
        adjacent_edges[Y].append([cost, Y, X])

    queue = adjacent_edges[start]
    heapq.heapify(queue)

    while queue:
        cost, x, y = heapq.heappop(queue)
        if y not in connected_nodes:
            connected_nodes.add(y)
            mst.append([x, y, cost])

            for edge in adjacent_edges[y]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(queue, edge)
        print(queue)

    return mst

print(prim(0, myedges))



