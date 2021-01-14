def solution(s):
    length = len(s)
    result = []
    if len(s) == 1:
        return 1

    for i in range(1, (length//2)+1):
        stack = []

        for j in range(0, len(s)+1, i):
            if not stack:
                stack.append([s[j:j+i], 1])
                continue

            if stack[-1][0] == s[j:j+i]:
                stack[-1][1] += 1
                continue

            else:
                stack.append([s[j:j+i], 1])
        result.append(len("".join(str(cnt) + s if cnt > 1 else s for s, cnt in stack)))
    return min(result)


s = "a"
print(solution(s))
