from loop_benchmarks import single_loop, nested_loop
from factorial_algorithms import factorial_recursive, factorial_iterative

if __name__ == "__main__":
    for n in [100, 500, 1000]:
        print(n, single_loop(n), nested_loop(n))
        print(n, factorial_iterative(n))
