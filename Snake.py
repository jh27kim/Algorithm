N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
movement = [list(input().split()) for _ in range(L)]

movement.insert(0, [0, "D"])
movement.append([100000, movement[-1][-1]])
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

x, y, answer = 0, 0, 0
snake = [[x, y]]
done = False
ind = -1


for i in range(len(movement)-1):
    t = int(movement[i+1][0]) - int(movement[i][0])
    if movement[i][1] == "D":
        ind += 1
    else:
        ind -= 1
    m = direction[ind % 4]
    if done:
        break
    while t:
        nx, ny = x + m[0], y + m[1]
        answer += 1
        if nx >= N or nx < 0 or ny >= N or ny < 0 or [nx, ny] in snake:
            done = True
            print(answer)
            break
        else:
            if [nx+1, ny+1] in apples:
                for a in range(len(apples)):
                    if [nx+1, ny+1] == apples[a]:
                        del apples[a]
                        #print(apples)
                        break
            else:
                snake.pop(0)
            snake.append([nx, ny])
            x, y = nx, ny
        t -= 1

