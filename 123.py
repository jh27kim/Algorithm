def solution(n):
    answer = ''
    nums = ['1', '2', '4']
    three = 3
    while True:
        n -= three
        three = three * 3
        if n <= 0:
            three = three // 3
            ind = three + n-1
            while three > 1:
                q, r = divmod(ind, 3)
                ind = q
                three = three // 3
                answer += nums[r]
            break

    return answer[::-1]

print(solution(10))
