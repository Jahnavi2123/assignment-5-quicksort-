# Assignment 5 – Quicksort Algorithm: Implementation, Analysis, and Randomization

## Overview

This project implements two versions of the Quicksort algorithm using Python.

The first implementation uses a deterministic approach where the first element of each subarray is selected as the pivot. The second implementation uses a randomized approach that selects a pivot randomly before partitioning. The goal of this assignment is to compare how these two approaches behave under different input conditions and understand how pivot selection affects performance.

In addition to the implementations, a benchmarking program is included to compare execution times on different dataset sizes and distributions.

---

## Files Included

- `deterministic_quicksort.py`
  - Implements Quicksort using the first element as the pivot.

- `randomized_quicksort.py`
  - Implements Quicksort using a randomly selected pivot.

- `benchmark.py`
  - Measures and compares the running times of both implementations using random, sorted, and reverse-sorted datasets.

- `report.md`
  - Describes the implementation, complexity analysis, benchmark discussion, and observations.

---

## Requirements

- Python 3.10 or newer

No external libraries are required.

---

## How to Run

Run the deterministic implementation:

```bash
python deterministic_quicksort.py
```

Run the randomized implementation:

```bash
python randomized_quicksort.py
```

Run the benchmark:

```bash
python benchmark.py
```

---

## Benchmark Datasets

The benchmark compares both algorithms using three different input distributions.

- Random integers
- Sorted integers
- Reverse-sorted integers

Each distribution is tested with increasing input sizes to observe how performance changes.

---

## Summary of Findings

The deterministic implementation performs well on random input but becomes much slower when the input is already sorted or reverse sorted because the pivot selection creates highly unbalanced partitions.

The randomized implementation performs much more consistently across all datasets because randomly selecting the pivot makes it much less likely that poor partitions will occur repeatedly.

Although both implementations have the same average-case time complexity of **O(n log n)**, randomization makes the algorithm much more reliable for real-world applications where the input order cannot always be predicted.

## Results

The complete benchmark table and detailed discussion are available in
[report.md](report.md).