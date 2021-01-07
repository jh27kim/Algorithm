N, M = map(int, input().split())
lessons = list(map(int, input().split()))
left, right = max(lessons), sum(lessons)


def correctAnswer(capacity):
    s = 0
    cnt = 0
    for i in range(len(lessons)):
        if s + lessons[i] <= capacity:
            s += lessons[i]
        else:
            s = lessons[i]
            cnt += 1
    if s:
        cnt += 1
    return True if cnt <= M else False


while left <= right:
    mid = (left + right) // 2

    if correctAnswer(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)

