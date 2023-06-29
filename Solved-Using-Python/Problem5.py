from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given a list of integers nums, find the majority element that appears more than n/2 times and return it.
        If there is no majority element, return -1.

        Args:
            nums: A list of integers.

        Returns:
            The majority element if it exists, otherwise -1.

        Example:
            Input: [2, 2, 1, 1, 1, 2, 2]
            Output: 2
            Explanation: The element 2 appears more than n/2 times (in this case, more than 7/2 = 3 times).

        """

        n = len(nums)
        cnt = 0
        element = None

        # Find a potential majority element
        for i in range(n):
            if cnt == 0:
                cnt = 1
                element = nums[i]
            elif element == nums[i]:
                cnt += 1
            else:
                cnt -= 1

        # Check if the potential majority element is a true majority
        cnt_occurrences = 0
        for i in range(n):
            if nums[i] == element:
                cnt_occurrences += 1

        if cnt_occurrences > (n / 2):
            return element
        return -1
