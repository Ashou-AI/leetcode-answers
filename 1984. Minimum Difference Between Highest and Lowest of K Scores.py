class Solution:
    """
    Approach 1: Sliding Window
    time: O(nlogn)
    space: O(nlogn), space: O(logn)
    """
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
