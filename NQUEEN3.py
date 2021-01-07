def dfs(col, diag1, diag2, n, d):
    global answer
    if d == n:
        answer += 1
        return
    for x in range(n):
        if x in col or (x+d) in diag1 or (x-d) in diag2:
            continue
        col.add(x)
        diag1.add(x+d)
        diag2.add(x-d)
        dfs(col, diag1, diag2, n, d+1)
        col.remove(x)
        diag1.remove(x+d)
        diag2.remove(x-d)


def solution(n):
    global answer
    answer = 0
    col, diag1, diag2 = set(), set(), set()
    dfs(col, diag1, diag2, n, 0)
    return answer

print(solution(4))