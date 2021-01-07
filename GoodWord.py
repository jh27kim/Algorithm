n = int(input())
answer = 0

for i in range(n):
    string = input()
    stack = [string[0]]
    for j in range(1, len(string)):
        if len(stack) == 0:
            stack.append(string[j])
            continue
        if stack[-1] == string[j]:
            stack.pop()
        else:
            stack.append(string[j])
    if len(stack) == 0:
        answer += 1
print(answer)
