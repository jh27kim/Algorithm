import string
word = input()

alphabets = dict(zip((list(string.ascii_lowercase)), ([0 for i in range(26)])))
for i in word:
    if i in alphabets:
        alphabets[i] += 1

print(*alphabets.values(), sep=' ')
