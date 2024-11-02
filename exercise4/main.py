import sys
from functions import *

X, Y, Z = 0, 5, 6

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <n>")
        sys.exit(1)

    n = int(sys.argv[1])

    if n < 0:
        print("n must be a positive integer")
        sys.exit(1)

    alpha: int = ((X + Y) % 5) + 3
    beta: int = ((Y + Z) % 5) + 3

    res_iter = F_iterative(alpha, beta, n)
    res_rec = F_recursive(alpha, beta, n)
    res_tail = F_tail(alpha, beta, n)

    print(f"Resultado iterativo: {res_iter}")
    print(f"Resultado recursivo: {res_rec}")
    print(f"Resultado tail: {res_tail}")

if __name__ == "__main__":
    main()
    