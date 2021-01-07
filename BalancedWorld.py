while True:
    string = input()
    brackets, stack = [], []
    if string == ".":
        break
    for i in string:
        if i == ")" or i == "(" or i == "[" or i == "]":
            brackets.append(i)
    for j in brackets:
        if stack:
            if (stack[-1] == "(" and j == ")") or (stack[-1] == "[" and j == "]"):
                stack.pop()
                continue
        stack.append(j)
    if stack:
        print('no')
    else:
        print('yes')
