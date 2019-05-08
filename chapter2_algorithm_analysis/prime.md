# Primality Test

## Square root theory

> $n={a}\times{b}$ if $n$ is not a prime, the theory is :
> $$\min(a,b)\leq\sqrt{n}$$

### Proof

It is very simple to prove by contradiction. If $\min(a,b)\gt\sqrt{n}$, ${a}\times{b}\gt{n}$ that is not correct.

## Sieve of Erastothenes 

> Sieve of Erastothenes is a method used to compute all primes less than N. The algorithm is described as follows:

1. generate all numbers from 2 to N
2. i values from 2 to $\sqrt{N}$ and i is a prime when i is not deleted
3. delete all numbers less than N which are multiples of i, i.e. multiples from 2 to N/i
4. the rest of the numbers are all primes less than N

### Proof

$i$ is a prime if $i$ is not deleted when $i$ goes up to $\sqrt{N}$ from 2 at step 1

> First of all it is very clear that a prime number will not be deleted since it is not a multiple of any number except 1 and itself. 

So if $i$ is not a prime, we can write $i=a\times{b}$ and $a$ is a prime less than or equal to $b$. $i$ will be deleted when deleting all multiples of $a$ less than N. That's it.

### Complexity

> For each prime number $p_j \leq{\sqrt{N}}$, we cross out at most $\frac{N}{p_j}$, so we get the following number of operations:

$$
n\times{(\frac{1}{2}+\frac{1}{3}+...)}=O(n\times\log{\log{n}})
$$

## Some usefule links

1. [Harmonic number](https://en.wikipedia.org/wiki/Harmonic_number)
2. [Divergence of the sum of the reciprocals of the primes](https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes)
3. [Time complexity of Sieve of Eratosthenes algorithm](https://stackoverflow.com/questions/2582732/time-complexity-of-sieve-of-eratosthenes-algorithm)
4. [Sieve of Eratosthenes Having Linear Time Complexity](https://cp-algorithms.com/algebra/prime-sieve-linear.html)