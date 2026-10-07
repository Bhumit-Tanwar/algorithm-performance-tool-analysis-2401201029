import matplotlib.pyplot as plt

def plot_benchmark(df, output_dir="graphs"):
    """Create execution-time and memory charts."""
    algorithms = df["algorithm"].unique()

    plt.figure(figsize=(9, 5))
    for algo in algorithms:
        subset = df[df["algorithm"] == algo]
        plt.plot(subset["input_size"], subset["time_sec"], marker="o", label=algo)
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Benchmarking Engine: Execution Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/benchmark_time.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    for algo in algorithms:
        subset = df[df["algorithm"] == algo]
        plt.plot(subset["input_size"], subset["memory_kb"], marker="s", label=algo)
    plt.xlabel("Input Size (n)")
    plt.ylabel("Peak Memory (KB)")
    plt.title("Benchmarking Engine: Memory Usage Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/benchmark_memory.png", dpi=150)
    plt.close()
