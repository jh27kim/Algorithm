N, M = map(int, input().split())
book = dict()
answer = []

for i in range(1, N+1):
    pokemon = input().rstrip()
    book[pokemon] = i

for j in range(M):
    quiz = input().rstrip()
    if quiz.isdigit():
        answer.append(list(book.keys())[int(quiz)-1])
    else:
        answer.append(book[quiz])

print(*answer, sep = '\n')