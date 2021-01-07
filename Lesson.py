N, K = map(int, input().split())
words, queue = [], []
offset, letters = set(), set()
offset.update(['a', 'n', 't', 'i', 'c'])
visited = []
answer = 0

for i in range(N):
    words.append(set(list(input()))-offset)

for w in words:
    letters.update(w)


def sol(n):
    global answer
    if n == K-len(offset):
        answer = max(answer, cnt())

    for l in letters:
        if l not in visited:
            queue.append(l)
            visited.append(l)
            sol(n + 1)
            queue.pop()
            visited.pop()


def cnt():
    result = 0
    for w in words:
        if all(elem in w for elem in queue):
            result += 1
    return result


if K < len(offset):
    print(0)
else:
    sol(0)
    print(answer)
