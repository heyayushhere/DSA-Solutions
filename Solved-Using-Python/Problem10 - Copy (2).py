# Problem Statement: Print all possible subsets of a given array using recursion.

def Print(i, d, a, n):
    """
    This function recursively prints all possible subsets of a given array.

    Args:
    - i: The current index being considered.
    - d: The current subset being formed.
    - a: The input array.
    - n: The length of the array.

    Returns:
    This function does not return any value explicitly but prints the subsets.

    """
    if i == n:
        # Base case: If the current index is equal to the length of the array,
        # we have considered all elements, so we print the current subset and return.
        print(d)
        if len(d) == 0:
            print("{}")
        return

    # Recursive call without including the element at the current index.
    Print(i + 1, d, a, n)

    # Recursive call including the element at the current index.
    d.append(a[i])
    Print(i + 1, d, a, n)

    # Backtracking: Remove the last element from the current subset before going back to the previous level.
    d.pop()

# Test the function with a sample array.
array = [1, 2, 3]
Print(0, [], array, len(array))
