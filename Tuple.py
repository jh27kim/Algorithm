def solution(s):
    s = s[1:len(s)-1]
    numbers = []
    answer = []
    for i in range(len(s)):
        if s[i] == "{":
            num = ""
            temp = []
            while True:
                i += 1
                if s[i].isnumeric():
                    num += s[i]
                elif s[i] == ",":
                    temp.append(int(num))
                    num = ""
                elif s[i] == "}":
                    temp.append(int(num))
                    numbers.append(temp)
                    break
    numbers.sort(key=lambda x:len(x))

    for j in range(len(numbers)):
        for k in numbers[j]:
            if k not in answer:
                answer.append(k)
    return answer


s = "{{20,111},{111}}"
print(solution(s))
