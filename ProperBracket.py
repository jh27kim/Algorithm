def solution(s):
    queue = []
    for i in range(len(s)):
        if not queue:
            queue.append(s[i])
            continue
        if queue[-1] == "(" and s[i] == ")":
            queue.pop()
        else:
            queue.append(s[i])
    if queue:
        return False
    else:
        return True

s = ")()("
print(solution(s))