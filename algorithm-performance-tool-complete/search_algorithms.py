import time

def linear_search(arr, target):
    """Return (index, comparisons)."""
    comparisons = 0
    for i, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    """Return (index, comparisons). arr must be sorted."""
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 7]
    print("Linear:", linear_search(data, 9))
    sorted_data = sorted(data)
    print("Binary:", binary_search(sorted_data, 9))
