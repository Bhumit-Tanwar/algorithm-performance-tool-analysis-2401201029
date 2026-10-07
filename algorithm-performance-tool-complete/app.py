import streamlit as st
import pandas as pd
import numpy as np
from search_algorithms import linear_search, binary_search
from loop_benchmarks import single_loop, nested_loop
from factorial_algorithms import factorial_recursive, factorial_iterative
from benchmark_engine import BenchmarkEngine
from visualization import plot_benchmark

st.set_page_config(page_title="Algorithm Performance Tool", layout="wide")
st.title("Algorithm Performance Measurement & Benchmarking Tool")
st.caption("DAA Lab 2")

algo = st.selectbox(
    "Select algorithm / program",
    ["Linear Search", "Binary Search", "Single Loop",
     "Nested Loop", "Recursive Factorial", "Iterative Factorial"]
)
n = st.number_input("Input size", min_value=1, max_value=50000, value=1000, step=100)

if st.button("Run Benchmark"):
    engine = BenchmarkEngine()

    if algo == "Linear Search":
        arr = list(range(int(n)))
        idx, comps = linear_search(arr, -1)
        st.write({"Result": idx, "Comparisons": comps})
        engine.run(linear_search, [int(n)], name=algo,
                   arg_builder=lambda x: (list(range(x)), -1),
                   operation_counter=lambda x: x)
    elif algo == "Binary Search":
        engine.run(binary_search, [int(n)], name=algo,
                   arg_builder=lambda x: (list(range(x)), -1),
                   operation_counter=lambda x: int(np.ceil(np.log2(x + 1))))
    elif algo == "Single Loop":
        engine.run(single_loop, [int(n)], name=algo,
                   operation_counter=lambda x: x)
    elif algo == "Nested Loop":
        engine.run(nested_loop, [int(n)], name=algo,
                   operation_counter=lambda x: x * x)
    elif algo == "Recursive Factorial":
        safe_n = min(int(n), 900)
        engine.run(factorial_recursive, [safe_n], name=algo,
                   operation_counter=lambda x: x)
    else:
        engine.run(factorial_iterative, [int(n)], name=algo,
                   operation_counter=lambda x: max(0, x - 1))

    st.dataframe(engine.as_dataframe(), use_container_width=True)
