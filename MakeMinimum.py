def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum(x[0]*x[1] for x in zip(A, B))


A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))