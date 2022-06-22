input_str = "IX MIII /"
output = "MXXVII"

num_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
digit_dict = {"I":1, "V":1, "X":2, "L":2, "C":3, "D":3, "M":4}
numbers = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
           ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
           ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
           ["", "M", "MM", "MMM"]]
exception = ["IX", "XC", "CM"]


def convertToRoman(num):
    result = ""

    for d in [3, 2, 1, 0]:
        q, r = divmod(num, 10**d)
        result += numbers[d][q]
        num = r

    return result


def convert(string):
    res = 0
    inverse = False
    for i in range(len(string)):
        if inverse:
            res = (-1 * res)
        if i+1 < len(string):
           if num_dict[string[i]] < num_dict[string[i+1]]:
                inverse = True
        res += num_dict[string[i]]

    return res


def convertToNumber(r):
    lst = []
    s = 0
    for i in range(len(r)):
        if not lst:
            lst.append(r[i])
            continue
        if digit_dict[r[i]] == digit_dict[lst[-1]]:
            lst.append(r[i])
            continue
        elif len(lst) == 1 and lst[-1] + r[i] in exception:
            lst.append(r[i])
            s += convert("".join(lst))
            lst = []
        elif digit_dict[r[i]] != digit_dict[lst[-1]]:
            s += convert("".join(lst))
            lst = [r[i]]

    if lst:
        s += convert("".join(lst))

    return s


a1, b1, op = input().split(" ")
a = convertToNumber(a1)
b = convertToNumber(b1)
if op == "+":
    print(convertToRoman((a + b) % 4000))

if op == "-":
    r = convertToRoman(abs(a - b) % 4000)
    if b > a:
        print("-" + str(r))
    else:
        print(r)

if op == "*":
    print(convertToRoman((a * b) % 4000))

if op == "/":
    print(convertToRoman((a // b) % 4000))