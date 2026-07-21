from typing import List


def deterministic_quicksort(values: List[int]) -> List[int]:
    """
    Sort a list using deterministic Quicksort.

    The first element is selected as the pivot. A copy is returned so
    the original input list is not modified.
    """
    result = values.copy()

    if len(result) < 2:
        return result

    _quicksort(result, 0, len(result) - 1)
    return result


def _quicksort(values: List[int], low: int, high: int) -> None:
    """
    Recursively sort the section values[low:high + 1].
    """
    if low >= high:
        return

    pivot_index = _partition(values, low, high)

    _quicksort(values, low, pivot_index - 1)
    _quicksort(values, pivot_index + 1, high)


def _partition(values: List[int], low: int, high: int) -> int:
    """
    Partition the array using the first element as the pivot.
    """
    pivot = values[low]
    boundary = low + 1

    for index in range(low + 1, high + 1):
        if values[index] < pivot:
            values[boundary], values[index] = values[index], values[boundary]
            boundary += 1

    pivot_index = boundary - 1
    values[low], values[pivot_index] = values[pivot_index], values[low]

    return pivot_index


if __name__ == "__main__":
    sample = [8, 3, 1, 7, 0, 10, 2]

    print("Original:", sample)
    print("Sorted:", deterministic_quicksort(sample))