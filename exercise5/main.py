from sympy import binomial, floor, log, tribonacci
import sys

n = int(sys.argv[1])
k = floor(log(n,2))

print(f"k: {k}")

Narayana = binomial(n, k) * binomial(n, k - 1) / n

print(f"Narayana: {Narayana}")

tribonacci_index=floor(log(binomial(n, k) * binomial(n, k - 1) / n, 2))

print(tribonacci(tribonacci_index + 1) + tribonacci(tribonacci_index))
