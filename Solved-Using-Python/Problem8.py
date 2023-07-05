# Problem Statement: Reverse the elements of a given list using recursion.

def reverse_sublist(arr, start, end):
    """
    This function recursively reverses a sublist within a given list.

    Args:
    - arr: The list in which the sublist needs to be reversed.
    - start: The starting index of the sublist.
    - end: The ending index of the sublist.

    Returns:
    The function does not return any value explicitly, but modifies the original list in-place.

    """
    if start >= end:
        # Base case: If the start index becomes greater than or equal to the end index,
        # the sublist has been reversed completely, so we stop the recursion.
        return
    
    # Swapping the elements at the start and end indices to reverse the sublist.
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursively calling the function with the updated start and end indices to reverse the remaining sublist.
    reverse_sublist(arr, start + 1, end - 1)

# Test the function with a sample list.
arr = [1, 2, 3, 4, 5]
reverse_sublist(arr, 0, len(arr) - 1)
print(arr)
