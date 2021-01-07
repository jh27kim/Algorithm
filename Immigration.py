def solution(n, times):
    answer = 0
    guards = len(times)
    end = ((n//guards)+1) * max(times)
    start = 1
    while start <= end:
        mid = (start + end) // 2
        time = sum(mid//x for x in times)
        if time < n:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
    return answer


n= 6
times = [7, 10]
#print(solution(n, times))


