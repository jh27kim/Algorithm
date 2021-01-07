def gcd(n, m):
    return m if n % m == 0 else gcd(m, n%m)

def solution(w,h):
    return w*h - (w + h - gcd(max(w, h), min(w, h)))


w = 8
h = 12
print(solution(w, h))