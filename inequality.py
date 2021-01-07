k = int(input())
string = list(input().split())

start = list(range(k+1))
end = list(reversed(range(10-k-1, 10)))


def convert(lst):
    s = [str(i) for i in lst]
    res = int("".join(s))
    return res


def sol(start, end, step):
    for i in range(convert(start), convert(end), step):
        ind = True
        num = list(str(i))
        if len(num) != k + 1:
            num.insert(0, "0")
        ans = num
        num = [int(k) for k in num]
        if len(set(num)) != k + 1:
            continue
        for j in range(len(num)-1):
            if (string[j] == "<" and num[j] > num[j+1]) or (string[j] == ">" and num[j] < num[j+1]):
                ind = False
                break
        if ind:
            print("".join(ans))
            break


sol(end, start, -1)
sol(start, end, 1)


