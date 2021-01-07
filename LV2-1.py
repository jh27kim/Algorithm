def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    d = []
    for i in range(len(numbers)):
        j = numbers[i]
        while len(j) < 4:
            j = j + j
        d.append([numbers[i], j])
    d.sort(key=lambda x:x[1], reverse=True)
    for s in d:
        answer += s[0]
    return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return "".join(numbers)

numbers = [0,0,0]
print(solution(numbers))