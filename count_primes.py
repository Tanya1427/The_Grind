# Use linked list for Euler's 

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [0, 0] + [*range(2, n)]
        n = len(primes)
        for p in primes:
            if p == 0:
                continue
            if p**2 > n:
                break
            for composite_index in range(p**2, n, p):
                primes[composite_index] = 0  # Mark as composite

        return sum(map(bool, primes))


"""Plan
Sieve Of Eratosthenes
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
"""
