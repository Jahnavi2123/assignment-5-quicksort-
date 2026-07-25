# Assignment 5
# Quicksort Algorithm: Implementation, Analysis, and Randomization

## Introduction

Quicksort is one of the most widely used sorting algorithms because it combines efficiency with a relatively simple implementation. The basic idea is to choose one element as a pivot, divide the remaining elements into smaller and larger groups, and then recursively apply the same process to each group. Although the algorithm is simple to understand, its performance depends heavily on how the pivot is selected.

For this assignment, I implemented two versions of Quicksort. The first version always selects the first element as the pivot, while the second version randomly selects a pivot before partitioning the array. After implementing both versions, I compared their performance using different input sizes and data distributions to better understand how pivot selection affects efficiency.

---

# Implementation

## Deterministic Quicksort

The deterministic implementation always chooses the first element of the current subarray as the pivot. After selecting the pivot, the algorithm scans the remaining elements and moves every value smaller than the pivot to the left side of the array. Once every element has been examined, the pivot is placed between the smaller and larger values. At that point, the pivot is already in its final sorted position.

The same process is then repeated recursively for the left and right portions of the array until every subarray contains zero or one element.

I chose this implementation because it clearly demonstrates both the strengths and weaknesses of Quicksort. While it performs very well on many inputs, it also shows how poor pivot selection can dramatically reduce performance.

---

## Randomized Quicksort

The randomized implementation follows the same partitioning process but changes how the pivot is selected. Instead of always using the first element, it randomly chooses one element from the current subarray and swaps it into the first position before partitioning begins.

This small modification greatly reduces the chance of repeatedly selecting extremely poor pivots. As a result, the randomized version usually produces more balanced partitions, leading to better performance on many different input distributions.

One advantage of this approach is that the algorithm no longer depends on the original ordering of the data. Even if the input is already sorted, the pivot selection remains unpredictable, making the worst-case behavior much less likely.

---

# Time Complexity Analysis

## Best Case

The best case occurs when each pivot divides the array into two nearly equal halves. Every level of recursion performs approximately **n** comparisons, and the recursion tree contains roughly **log n** levels.

Because the amount of work performed at each level is proportional to the number of elements, the overall running time becomes:

**O(n log n)**

Balanced partitions allow the algorithm to finish efficiently since the recursion depth remains relatively small.

---

## Average Case

The average case also runs in **O(n log n)**.

Although the pivot will not perfectly divide the array every time, random input usually produces reasonably balanced partitions. Although the pivot does not divide the array exactly in half every time, the partitions are reasonably balanced on average. Across the recursion tree, partitioning performs O(n) work for each approximate level, and the expected height of the tree is O(log n). Therefore, the expected running time is O(n log n).

---

## Worst Case

The worst case happens when every pivot is either the smallest or largest element in the current subarray.

Instead of splitting the array into two similar sections, one partition contains almost every element while the other is empty. This creates a recursion depth close to **n**, resulting in approximately:

n + (n − 1) + (n − 2) + ... + 1

operations.

This simplifies to:

**O(n²)**

Using the first element as the pivot makes sorted and reverse-sorted arrays particularly vulnerable to this behavior.

---

# Space Complexity

Quicksort performs partitioning directly inside the array instead of creating additional arrays during every recursive call. Because of this, the algorithm itself is considered an in-place sorting algorithm.

However, recursive function calls require stack space. When the partitions remain balanced, the recursion stack requires approximately **O(log n)** space. In the worst case, when the partitions become highly unbalanced, the recursion depth can increase to **O(n)**.

In my implementation, the original input list is copied before sorting so that the caller's data is preserved. This introduces additional memory usage beyond the recursive stack, but it also makes the functions easier to test because the original input remains unchanged.

---

# Impact of Randomization

Randomization does not change the theoretical worst-case complexity of Quicksort. It is still possible for the algorithm to repeatedly choose poor pivots.

However, the probability of selecting poor pivots throughout every recursive call is extremely small. Instead of depending on the original ordering of the input data, every partition starts with a randomly selected pivot. This makes highly unbalanced recursion much less common.

For this reason, randomized Quicksort is generally preferred in practical applications because it produces more predictable performance across different datasets.

---

# Empirical Analysis

The benchmark compared deterministic and randomized Quicksort using random, sorted, and reverse-sorted datasets of increasing size.

For random input, both implementations produced similar execution times because the first element was usually not an extremely poor pivot. Small differences between runs are expected because the randomized implementation selects different pivots each time.

The largest differences appeared when testing sorted and reverse-sorted datasets. Since the deterministic implementation always selected the first element as the pivot, it repeatedly generated highly unbalanced partitions. As the dataset became larger, this caused significantly deeper recursion and slower execution.

The randomized implementation behaved much more consistently because the pivot selection was independent of the original input order. Even when the data was already sorted, randomly selecting the pivot usually produced more balanced partitions and avoided the severe performance degradation seen in the deterministic version.

Overall, the benchmark results closely matched the theoretical analysis. The deterministic implementation demonstrated why pivot selection is important, while the randomized implementation showed how a small change can greatly improve the algorithm's practical performance.

## Benchmark Results

The benchmark was executed using random, sorted, and reverse-sorted datasets. Each reported value represents the median execution time across five runs.

## Benchmark Results

The benchmark compared the deterministic and randomized implementations of Quicksort using random, sorted, and reverse-sorted datasets. Each reported execution time represents the median of five runs.

| Input Size | Distribution | Deterministic Quicksort (seconds) | Randomized Quicksort (seconds) |
|------------:|--------------|----------------------------------:|-------------------------------:|
| 100 | Sorted | 0.000041 | 0.000024 |
| 100 | Reverse-Sorted | 0.000070 | 0.000024 |
| 500 | Random | 0.000124 | 0.000174 |
| 500 | Sorted | 0.001269 | 0.000248 |
| 500 | Reverse-Sorted | 0.002933 | 0.000276 |
| 1000 | Random | 0.000322 | 0.000372 |
| 1000 | Sorted | RecursionError | 0.000746 |
| 1000 | Reverse-Sorted | RecursionError | 0.000343 |
| 2000 | Random | 0.000632 | 0.000879 |
| 2000 | Sorted | RecursionError | 0.000764 |
| 2000 | Reverse-Sorted | RecursionError | 0.000754 |
| 5000 | Random | 0.001717 | 0.002228 |
| 5000 | Sorted | RecursionError | 0.002059 |
| 5000 | Reverse-Sorted | RecursionError | 0.001955 |

---

# Design Decisions

One design decision I made was to separate the deterministic and randomized implementations into different files. This made each implementation easier to understand and allowed the benchmarking program to compare them independently.

I also kept the partition logic simple and well documented instead of trying to optimize every line of code. My goal was to make the implementation easy to follow while still producing correct results.

Finally, I used a benchmarking script that automatically generated different input distributions. Testing random, sorted, and reverse-sorted datasets provided a better understanding of how input characteristics influence Quicksort's performance.

---

# Conclusion

This assignment demonstrated that Quicksort is not only affected by the number of elements being sorted but also by the way pivots are selected throughout the algorithm.

The deterministic implementation highlighted how poor pivot choices can lead to quadratic running time, especially when the input is already ordered. The randomized implementation showed that introducing randomness significantly reduces the likelihood of this behavior while maintaining the same expected time complexity.

Working through both implementations helped reinforce the relationship between algorithm design and practical performance. Although both versions share the same underlying algorithm, a relatively small implementation change produced noticeably more stable behavior across different datasets. This assignment also showed that evaluating an algorithm requires both theoretical analysis and experimental testing, since real-world performance depends on many factors beyond asymptotic complexity.

Therefore, although the partitioning process itself is in place, the complete implementation uses O(n) additional space because it creates a copy of the input list. The recursion stack adds O(log n) space in the average case and O(n) in the worst case.