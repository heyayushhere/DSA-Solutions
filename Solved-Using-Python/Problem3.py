from typing import List

class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
        """
        Given a list of integers 'n', return a list containing the squares of the numbers in sorted order.

        Example:
        Input: n = [-4, -2, 0, 2, 4]
        Output: [0, 4, 4, 16, 16]

        Explanation:
        The squares of the numbers in the input list are [16, 4, 0, 4, 16].
        After sorting, the resulting list is [0, 4, 4, 16, 16].

        Solution:
        1. Create an empty list 'm' to store the squared numbers.
        2. Iterate through each number 'i' in the input list 'n'.
        3. If 'i' is negative, square its absolute value and append it to 'm'.
           Otherwise, square 'i' itself and append it to 'm'.
        4. Sort the list 'm' in ascending order.
        5. Return the sorted list 'm'.
        """
        m = []  # List to store the squared numbers

        for i in n:
            if i < 0:
                m.append(abs(i) * abs(i))  # Square the absolute value of negative numbers
            else:
                m.append(i * i)  # Square positive numbers

        m.sort()  # Sort the list in ascending order

        return m
