import random
from typing import List


def randomized_quicksort(values: List[int]) -> List[int]:
    """
    Sort a list using randomized Quicksort.

    A random pivot is selected during every partition operation.
    Random pivot selection lowers the probability of repeatedly
    creating extremely unbalanced partitions.
    """

    # Work on a copy so the caller's original list is not modified.
    result = values.copy()

    # Empty lists and single-element lists require no sorting.
    if len(result) < 2:
        return result

    # Sort the complete copied list.
    _quicksort(result, 0, len(result) - 1)

    return result


def _quicksort(values: List[int], low: int, high: int) -> None:
    """
    Recursively sort the subarray from low through high.
    """

    # This condition prevents unnecessary recursive calls.
    if low >= high:
        return

    # Partition using a randomly selected pivot.
    pivot_index = _randomized_partition(values, low, high)

    # Recursively process the left partition.
    _quicksort(values, low, pivot_index - 1)

    # Recursively process the right partition.
    _quicksort(values, pivot_index + 1, high)


def _randomized_partition(
    values: List[int],
    low: int,
    high: int,
) -> int:
    """
    Select a random pivot and then partition the subarray.
    """

    # Choose any index within the active subarray.
    random_index = random.randint(low, high)

    # Move the selected pivot to the first position so the regular
    # partition function can process it consistently.
    values[low], values[random_index] = (
        values[random_index],
        values[low],
    )

    return _partition(values, low, high)


def _partition(values: List[int], low: int, high: int) -> int:
    """
    Rearrange the subarray around the pivot stored at index low.
    """

    # Store the pivot value before performing swaps.
    pivot = values[low]

    # Boundary tracks the first position not yet occupied by
    # a value smaller than the pivot.
    boundary = low + 1

    # Compare each remaining value with the pivot.
    for index in range(low + 1, high + 1):

        # Smaller values are moved into the left partition.
        if values[index] < pivot:
            values[boundary], values[index] = (
                values[index],
                values[boundary],
            )
            boundary += 1

    # Calculate the position where the pivot should be placed.
    pivot_index = boundary - 1

    # Move the pivot between the smaller and larger partitions.
    values[low], values[pivot_index] = (
        values[pivot_index],
        values[low],
    )

    return pivot_index


if __name__ == "__main__":
    sample = [8, 3, 1, 7, 0, 10, 2]

    print("Original:", sample)
    print("Sorted:", randomized_quicksort(sample))