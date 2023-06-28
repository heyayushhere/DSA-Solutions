"""
Problem Statement:
Given an array 'a' of integers and an integer 'k', rotate the array to the right by 'k' steps in-place.

Example:
Input: a = [1, 2, 3, 4, 5], k = 3
Output: [3, 4, 5, 1, 2]

Explanation:
The array [1, 2, 3, 4, 5] is rotated to [3, 4, 5, 1, 2] by 3 steps to the right.

Solution:
The rotation operation can be performed by reversing different parts of the array in-place.

"""

from typing import List

class Solution:
    @staticmethod
    def reverse(a, st, b):
        """
        Reverses the elements in the array 'a' from index 'st' to index 'b' (both inclusive).
        """
        n = len(a)
        s = st
        e = b - 1
        while s <= e:
            a[s], a[e] = a[e], a[s]
            s += 1
            e -= 1
    
    def rotate(self, a: List[int], k: int) -> None:
        """
        Rotate the array 'a' to the right by 'k' steps in-place.
        """
        k = k % len(a)  # Adjust 'k' to handle cases where 'k' is greater than the length of 'a'
        
        # Reverse the first part of the array
        Solution.reverse(a, 0, len(a) - k)
        
        # Reverse the second part of the array
        Solution.reverse(a, len(a) - k, len(a))
        
        # Reverse the entire array
        Solution.reverse(a, 0, len(a))
