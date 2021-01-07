def solution(n, stations, w):
    blanks = []
    visited = [0 for _ in range(n)]
    answer = 0
    for s in stations:
        start, end = s - 1 - w, s - 1 + w
        if end >= n:
            end = n - 1
        if start < 0:
            start = 0
        for i in range(start, end + 1):
            visited[i] = 1

    temp = []
    cnt = 0
    for x in range(n):
        if visited[x]:
            if cnt:
                blanks.append(cnt)
                cnt = 0
        else:
            cnt += 1
    if visited[-1] == 0:
        blanks.append(cnt)

    for i in blanks:
        q, r = divmod(i, w * 2 + 1)
        answer += q
        if r:
            answer += 1

    return answer

N = 11
stations = [4, 11]