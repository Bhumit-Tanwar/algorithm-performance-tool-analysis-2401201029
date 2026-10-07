# Algorithm Performance Measurement and Benchmarking Tool

DAA Lab Assignment 2 — BCA (AI&DS), Semester V

## Features
- Linear Search and Binary Search
- Single Loop and Nested Loop
- Recursive and Iterative Factorial
- Automated execution-time and peak-memory measurement
- Operation-count estimates for applicable algorithms
- Complexity comparison table
- Performance graphs
- Streamlit interface

## Run
```bash
python -m venv venv
# Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Repository structure
- `app.py` — Streamlit application
- `search_algorithms.py` — search implementations
- `loop_benchmarks.py` — loop implementations
- `factorial_algorithms.py` — factorial implementations
- `benchmark_engine.py` — reusable benchmark engine
- `visualization.py` — chart generation
- `benchmark_results.csv` — sample benchmark output
- `graphs/` — generated charts
- `project_notebook.ipynb` — notebook


## Detailed Execution Workflow

1. Activate the virtual environment.
2. Install dependencies from `requirements.txt`.
3. Run `python benchmark_engine.py` for batch measurements.
4. Inspect `benchmark_results.csv`.
5. Generate or update charts using `visualization.py`.
6. Run `streamlit run app.py` for the interactive interface.
7. Review the final report before GitHub submission.

## Benchmark Interpretation

The measured values are experimental observations and can change with hardware, Python version,
operating-system load and repeated-run conditions. The most important comparison is the growth trend
as input size increases.

## Academic Submission Preparation

Before final submission, replace the student-name and roll-number placeholders, run the benchmark
on the computer being used for submission, capture screenshots of the application and outputs, and
push the complete project to the private GitHub repository.
