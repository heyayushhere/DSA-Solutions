# Problem Statement:
# Given an array of integers 'arr' and a target integer 'target', the task is to determine whether there are two elements in the array whose sum equals the target.
# If such a pair exists, return "YES"; otherwise, return "NO".

def twoSum(n, arr, target):
    arr.sort()  # Sorting the array in ascending order
    left = 0
    right = n - 1
    while left < right:
        _sum = arr[left] + arr[right]
        if _sum == target:
            return "YES"  # Pair found
        elif _sum < target:
            left += 1  # Increment left pointer to increase the sum
        else:
            right -= 1  # Decrement right pointer to decrease the sum
    return "NO"  # Pair not found

# Example usage:
n = 5  # Size of the array
arr = [2, 7, 11, 15, 3]  # Array of integers
target = 9  # Target sum

result = twoSum(n, arr, target)
print(result)
