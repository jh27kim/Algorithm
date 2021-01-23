'''
def check(w1, w2):
    for i in range(len(w1)):
        if w1[i] == w2[i] or w1[i] == '?':
            continue
        else:
            return 0
    return 1


def solution(words, queries):
    answer = []
    for q in queries:
        count = 0
        for word in words:
            if len(word) != len(q):
                continue
            count += check(q, word)
        answer.append(count)

    return answer
'''
import bisect


def count_by_range(lst, left_value, right_value):
    left = bisect.bisect_left(lst, left_value)
    right = bisect.bisect_right(lst, right_value)
    return right - left


def solution(words, queries):
    lst = [[] for _ in range(10001)]
    reversed_lst = [[] for _ in range(10001)]
    answer = []

    for word in words:
        lst[len(word)].append(word)
        reversed_lst[len(word)].append(word[::-1])

    for l in range(10001):
        lst[l].sort()
        reversed_lst[l].sort()

    for q in queries:
        if q[0] == '?':
            res = count_by_range(reversed_lst[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        else:
            res = count_by_range(lst[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        answer.append(res)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))