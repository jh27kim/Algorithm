s = input()
b = list(s)
a = reversed(s)

if b == list(a):
    print('1')
else:
    print('0')