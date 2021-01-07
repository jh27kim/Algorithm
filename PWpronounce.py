vowels = ['a', 'e', 'i', 'o', 'u']
result = []
Strings = []
acc = ["acceptable.", "not acceptable."]

while True:
    s = input()
    if s == "end":
        break
    Strings.append(s)

    if not(any(x in vowels for x in s)):
        result.append(False)
        continue

    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            if s[i] != 'e' and s[i] != 'o':
                result.append(False)
                break
        if i >= 2:
            if s[i] in vowels and s[i-1] in vowels and s[i-2] in vowels:
                result.append(False)
                break
            if s[i] not in vowels and s[i-1] not in vowels and s[i-2] not in vowels:
                result.append(False)
                break
    if len(result) != len(Strings):
        result.append(True)

for k in range(len(Strings)):
    if result[k]:
        print("<"+Strings[k]+">","is "+acc[0])
    else:
        print("<"+Strings[k]+">","is "+acc[1])