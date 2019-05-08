def is_prime(num):
    """
    trial division
    """
    if num <= 1:
        return False
    if num == 2:
        return True

    half_root = int(num ** 0.5)
    for i in range(2, half_root+1):
        if num % i == 0:
            return False
    return True

def sieve_erastothenes(N):
    nums = { n:n for n in range(2, N+1) }
    stop_at = int(N ** 0.5)
    for i in range(2, stop_at + 1):
        if i in nums:
            for j in range(2, N // i + 1):
                key = j * i
                if key in nums:
                    del nums[key]
    print(','.join(map(str, nums.keys())))

def sieve_erastothenes2(N):
    sieve = [True] * N
    sieve[0] = sieve[1] = False
    i = 2
    while( i ** 2 <= N ):
        if sieve[i]:
            k = i ** 2
            while k <= N:
                sieve[k] = False
                k += i
    return sieve

def main():
    sieve_erastothenes(100)

if __name__ == '__main__':
    main()