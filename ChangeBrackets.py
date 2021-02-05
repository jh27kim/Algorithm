def split(string):
    size = len(string)//2

    for i in range(1, size+1):
        cand = string[:i*2]
        cnt = 0
        for j in cand:
            if j == "(":
                cnt += 1
            else:
                cnt -= 1
        if cnt == 0:
            return cand, string[i*2:]


def check(string):
    stack = []
    for i in range(len(string)):
        if not stack:
            stack.append(string[i])
        else:
            if stack[-1] == "(" and string[i] == ")":
                stack.pop()
            else:
                stack.append(string[i])

    if stack:
        return False
    return True


def solution(p):
    if p == '':
        return p

    u, v = split(p)
    if check(u):
        return u + solution(v)
    else:
        new_string = "("
        new_string += solution(v)
        new_string += ")"

        new_u = u[1:len(u)-1]
        for i in new_u:
            if i == "(":
                new_string += ")"
            else:
                new_string += "("

        return new_string


p = "(()())()"
p = ")("
p = "()))((()"
print(solution(p))
