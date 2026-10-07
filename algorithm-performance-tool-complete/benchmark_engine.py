import time
import tracemalloc
import pandas as pd

class BenchmarkEngine:
    """Reusable engine for execution time, peak memory and operation counts."""

    def __init__(self):
        self.results = []

    def run(self, func, input_sizes, name=None, arg_builder=lambda n: (n,),
            operation_counter=None):
        algo_name = name or func.__name__

        for n in input_sizes:
            args = arg_builder(n)

            tracemalloc.start()
            start = time.perf_counter()
            func(*args)
            elapsed = time.perf_counter() - start
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            operations = None
            if operation_counter is not None:
                operations = operation_counter(n)

            self.results.append({
                "algorithm": algo_name,
                "input_size": n,
                "time_sec": elapsed,
                "memory_kb": peak / 1024,
                "operations": operations
            })
        return self

    def as_dataframe(self):
        return pd.DataFrame(self.results)
