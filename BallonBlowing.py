from heapq import nsmallest
from heapq import nlargest

def second_smallest(numbers, n):
    return nsmallest(n, numbers)[-1]


def solution(a):
    answer = 2
    if len(a) == 1 or len(a) == 2:
        return len(a)
    for i in range(1, len(a)-1):
        #왼쪽 > i < 오른쪽 가능
        secondLeft = second_smallest(a[:i], 2)
        secondRight = second_smallest(a[i+1:], 2)
        firstLeft = second_smallest(a[:i], 1)
        firstRight = second_smallest(a[i + 1:], 1)

        if secondLeft > a[i] and a[i] < firstRight:
            answer += 1
            continue
        if firstLeft > a[i] and a[i] < secondRight:
            answer += 1
            continue

        # 왼쪽 > i > 오른쪽 & 기회 1 가능
        if firstLeft > a[i] > firstRight:
            answer += 1
            continue
        if firstLeft > a[i] > firstRight:
            answer += 1
            continue

        #왼쪽 < i < 오른쪽 & 기회 1 가능
        if firstLeft < a[i] < firstRight:
            answer += 1
            continue
        if firstLeft < a[i] < firstRight:
            answer += 1
            continue
    return answer


a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))

print((nlargest(2, a)))