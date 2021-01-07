def solution(arr1, arr2):
    x1, y1, x2, y2 = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])
    answer = [[0 for _ in range(y2)] for _ in range(x1)]
    for i in range(x1):
        for j in range(y2):
            ind = 0
            a = 0
            while ind < y1:
                a += arr1[i][ind] * arr2[ind][j]
                ind += 1
            answer[i][j] = a
    return answer


arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1, arr2))
