import numpy

def gcd(m, n):
    if m < n:
        m, n = n, m
    while n > 0:
        rem = m % n
        m = n
        n = rem
    return m

def main():
    print(gcd(214213948, 234092))

if __name__ == '__main__':
    main()