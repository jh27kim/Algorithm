def solution(arr):
    answer = []
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
        i += 1
    answer.append(arr[-1])
    return answer


arr =[4,4,4,3,3]
print(solution(arr))