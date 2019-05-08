import time
import numpy

def power(x, n):
    """
    running time O(n)
    """
    if n == 0:
        return 1
    product = x
    for _ in range(n-1):
        product *= x
    return product

def efficient_power(x, n):
    """
    running time O(logn)
    """
    # base case
    if n == 0:
        return 1
    if n == 1:
        return x
    # even
    if n % 2 == 0:
        return efficient_power(x * x, n // 2)
    else:
        return efficient_power(x * x, n // 2) * x

def polynomial1(coefficients, base):
    """
    running time O(n)
    """
    poly = 0
    nomial = 1
    for i in range(len(coefficients)):
        poly += coefficients[i] * nomial
        nomial *= base
    return poly

def polynomial2(coefficients, base):
    """
    Horner's rule running time O(n) which is them same as polynomial1
    """
    nested = 0
    for i in range(len(coefficients))[::-1]:
        nested = coefficients[i] + base * nested
    return nested

def main():
    t = time.time()
    print(power(1, 100000))
    print(time.time() - t)

    t = time.time()
    print(efficient_power(1, 100000))
    print(time.time() - t)

    coefficients = numpy.random.randint(1, 100, 50000)
    numpy.random.shuffle(coefficients)

    t = time.time()
    print(polynomial1(coefficients, 1))
    print(time.time() - t)

    t = time.time()
    print(polynomial2(coefficients, 1))
    print(time.time() - t)

if __name__ == '__main__':
    main()