import sys
import random
import timeit
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from functions import *

X, Y, Z = 0, 5, 6

max_int: int = 3950

def check_time(n: int) -> List[float|int]:
    times = []
    alpha: int = ((X + Y) % 5) + 3
    beta: int = ((Y + Z) % 5) + 3
    for (i, num) in enumerate(range(1, max_int, max_int//n)):
        if i == n:
            break
        print(f"Test {i+1}/{n} with n = {num}")
        time_iter = timeit.timeit(lambda: F_iterative(alpha, beta, num), number=1)
        print("Iterative done")
        time_rec = timeit.timeit(lambda: F_recursive(alpha, beta, num), number=1)
        print("Recursive done")
        time_tail = timeit.timeit(lambda: F_tail(alpha, beta, num), number=1)
        print("Tail done")
        times.append((num, time_iter, time_rec, time_tail))
    return times

def write_csv(times: List[float|int]) -> None:
    with open("results.csv", "w") as f:
        f.write("n,iterative,recursive,tail\n")
        for n, time_iter, time_rec, time_tail in times:
            f.write(f"{n},{time_iter},{time_rec},{time_tail}\n")

def analyze_results() -> None:
    df = pd.read_csv("results.csv")
    print(df.describe())

    # Create a plot with the results
    plt.plot(df["n"], df["iterative"], label="Iterative")
    plt.plot(df["n"], df["recursive"], label="Recursive")
    plt.plot(df["n"], df["tail"], label="Tail")
    plt.legend()
    plt.xlabel("n")
    plt.ylabel("Time")

    # Save the plot
    plt.savefig("results.png")

def main():
    n_tests: int = int(sys.argv[1])
    times = check_time(n_tests)
    write_csv(times)
    analyze_results()

if __name__ == "__main__":
    main()
