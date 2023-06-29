from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Given a list of integers nums, find the contiguous subarray with the maximum product and return that product.

        Args:
            nums: A list of integers

        Returns:
            The maximum product of a contiguous subarray.

        Example:
            Input: [2, 3, -2, 4]
            Output: 6
            Explanation: The contiguous subarray [2, 3] has the maximum product of 6.

        """

        if not nums:
            return 0

        max_prod = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max
            max_prod = max(max_prod, max_so_far)

        return max_prod
