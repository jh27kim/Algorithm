def solution(A, B):
    bigger = []
    A.sort()

    for i in range(len(A)):
        val = B[i]
        left, right = 0, len(B) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < val:
                left = mid + 1
            else:
                right = mid
        if A[left] < val:
            left += 1

        bigger.append(left)
    print(bigger)
    bigger = [i if i < len(A) else len(A) for i in bigger]
    print(bigger)
    b = set(bigger)
    print(b)
    if 0 in b:
        return len(b) - 1
    return len(b)

A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A, B))