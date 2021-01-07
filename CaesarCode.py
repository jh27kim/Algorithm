s = "a B z"
n = 1
answer = ""
for k in s:
    if k.islower():
        print(ord(k) + n)
        answer += chr(((ord(k) + n - 97) % 26) + 97)
    elif k.isupper():
        answer += chr((((ord(k) + n - 65) % 26) + 65))
    else:
        answer += k
print(answer)
print(ord("a"))