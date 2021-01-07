def dfs(x, depth):
    if depth == 3:
        return
    for i in range(x, len(lst)):
        queue.append(lst[i])
        print(x)
        print(queue)
        dfs(i+1, depth+1)
        queue.pop()
        print(queue)


lst = [1, 2, 3, 4, 5]
for i in range(5):
    queue = []
    dfs(0, 0)
