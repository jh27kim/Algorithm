from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = []
    queue = deque()
    queue.append(begin)
    while queue:
        #print(queue)
        lenq = len(queue)
        while lenq:
            word = queue.popleft()
            if word == target:
                return answer
            for w in words:
                if check(word, w) and w not in visited:
                    queue.append(w)
                    visited.append(w)
            lenq -= 1
        answer += 1
    return answer


def check(w1, w2):
    move = True
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            if not move:
                return False
            move = False
    return True

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))