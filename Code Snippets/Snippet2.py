def max_subarray_sum(list1):
    """Finds the largest sum of a contiguous subarray in the given list.

    Args:
        list1: A list of numbers.

    Returns:
        The largest sum of a contiguous subarray in the given list.
    """

    max_so_far = 0
    current_max = 0
    for num in list1:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
    return max_so_far


if __name__ == "__main__":
    list1 = [1, 2, 3, -4, 5, 6]
    max_sum = max_subarray_sum(list1)
    print(max_sum)
