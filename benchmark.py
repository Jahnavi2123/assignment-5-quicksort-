import random
import statistics
import time
from typing import Callable, Dict, List, Optional

from deterministic_quicksort import deterministic_quicksort
from randomized_quicksort import randomized_quicksort


# This type alias describes any sorting function that receives
# a list of integers and returns a sorted list.
SortFunction = Callable[[List[int]], List[int]]


def measure_time(
    sort_function: SortFunction,
    values: List[int],
    trials: int = 5,
) -> Optional[float]:
    """
    Measure the median execution time of a sorting function.

    Running several trials reduces the effect of temporary system
    activity, such as background processes, on a single measurement.
    """

    execution_times: List[float] = []

    for _ in range(trials):

        # Each trial receives the same unsorted data.
        test_values = values.copy()

        try:
            # perf_counter provides a high-resolution timer suitable
            # for measuring short algorithm executions.
            start_time = time.perf_counter()

            result = sort_function(test_values)

            end_time = time.perf_counter()

        except RecursionError:
            # The deterministic version may exceed Python's recursion
            # limit on large sorted or reverse-sorted inputs.
            return None

        # Verify correctness before trusting the timing result.
        if result != sorted(values):
            raise ValueError(
                f"{sort_function.__name__} produced an incorrect result."
            )

        execution_times.append(end_time - start_time)

    # The median is less affected by unusually slow or fast trials.
    return statistics.median(execution_times)


def create_datasets(size: int) -> Dict[str, List[int]]:
    """
    Create datasets with different input distributions.
    """

    # Random data represents a typical unsorted input.
    random_values = [
        random.randint(0, size * 10)
        for _ in range(size)
    ]

    # Sorted input reveals the weakness of choosing the first element
    # as the pivot in deterministic Quicksort.
    sorted_values = list(range(size))

    # Reverse-sorted input also produces very unbalanced partitions
    # when the first element is always used as the pivot.
    reverse_values = list(range(size, 0, -1))

    return {
        "Random": random_values,
        "Sorted": sorted_values,
        "Reverse": reverse_values,
    }


def format_time(value: Optional[float]) -> str:
    """
    Convert timing values into a readable table entry.
    """

    if value is None:
        return "RecursionError"

    return f"{value:.6f}"


def run_benchmarks() -> None:
    """
    Compare both Quicksort versions across several input sizes.
    """

    sizes = [100, 500, 1000, 2000, 5000]

    print(
        f"{'Size':<8}"
        f"{'Distribution':<15}"
        f"{'Deterministic':<18}"
        f"{'Randomized':<18}"
    )

    for size in sizes:

        # Generate all three distributions for the current size.
        datasets = create_datasets(size)

        for distribution, values in datasets.items():

            # Measure the deterministic implementation.
            deterministic_time = measure_time(
                deterministic_quicksort,
                values,
            )

            # Measure the randomized implementation.
            randomized_time = measure_time(
                randomized_quicksort,
                values,
            )

            print(
                f"{size:<8}"
                f"{distribution:<15}"
                f"{format_time(deterministic_time):<18}"
                f"{format_time(randomized_time):<18}"
            )


if __name__ == "__main__":
    # A fixed seed makes the generated test data reproducible.
    random.seed(42)

    run_benchmarks()