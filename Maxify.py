import itertools


def sol(priorities, n, expression):
    if n == 2:
        return str(eval(expression))
    if priorities[n] == "*":
        res = eval("*".join([sol(priorities, n+1, e) for e in expression.split("*")]))
    if priorities[n] == "+":
        res = eval("+".join([sol(priorities, n+1, e) for e in expression.split("+")]))
    if priorities[n] == "-":
        res = eval("-".join([sol(priorities, n+1, e) for e in expression.split("-")]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = itertools.permutations(["*","-","+"], 3)
    for p in priorities:
        m = int(sol(p, 0, expression))
        answer = max(abs(m), answer)
    return answer


expression = "100-200*300-500+20"
print(solution(expression))
