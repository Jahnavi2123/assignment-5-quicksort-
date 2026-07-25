from typing import List


def deterministic_quicksort(values: List[int]) -> List[int]:
    """
    Sort a list using deterministic Quicksort.

    This version always selects the first element of the current
    subarray as the pivot. A copy of the input is created so that
    the original list remains unchanged.
    """

    # Copy the input because the helper function performs swaps in place.
    result = values.copy()

    # A list with zero or one element is already sorted.
    if len(result) < 2:
        return result

    # Begin sorting the full list, from index 0 to the final index.
    _quicksort(result, 0, len(result) - 1)

    return result


def _quicksort(values: List[int], low: int, high: int) -> None:
    """
    Recursively sort the portion of the list between low and high.
    """

    # Stop the recursion when the subarray contains zero or one element.
    if low >= high:
        return

    # Partition the current subarray and obtain the pivot's final position.
    pivot_index = _partition(values, low, high)

    # Sort the elements located to the left of the pivot.
    _quicksort(values, low, pivot_index - 1)

    # Sort the elements located to the right of the pivot.
    _quicksort(values, pivot_index + 1, high)


def _partition(values: List[int], low: int, high: int) -> int:
    """
    Partition a subarray using the first element as the pivot.

    After partitioning:
    - Values smaller than the pivot appear on the left.
    - The pivot is moved into its final sorted position.
    - Values greater than or equal to the pivot remain on the right.
    """

    # The deterministic version always chooses the first element as pivot.
    pivot = values[low]

    # Boundary marks the next position where a value smaller than
    # the pivot should be placed.
    boundary = low + 1

    # Examine every element after the pivot.
    for index in range(low + 1, high + 1):

        # Move smaller elements toward the left side of the subarray.
        if values[index] < pivot:
            values[boundary], values[index] = (
                values[index],
                values[boundary],
            )
            boundary += 1

    # The pivot belongs immediately before the first larger element.
    pivot_index = boundary - 1

    # Move the pivot into its final sorted position.
    values[low], values[pivot_index] = (
        values[pivot_index],
        values[low],
    )

    return pivot_index

test_cases = [
    [],
    [5],
    [3, 1, 2],
    [4, 4, 4, 4],
    [-3, 7, 0, -1, 5],
    [10, 9, 8, 7, 6],
]

for values in test_cases:
    assert deterministic_quicksort(values) == sorted(values)

print("All deterministic Quicksort tests passed.")


if __name__ == "__main__":
    sample = [8, 3, 1, 7, 0, 10, 2]

    print("Original:", sample)
    print("Sorted:", deterministic_quicksort(sample))