class Solution:
    """
    Approach 1: Binary Search
    time: O(nlogn), space: O(1)
    Requirement: space: O(1)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:  # interval: ( ]
            mid = (left+right)//2
            cnt = sum(num <= mid for num in nums)
            if cnt <= mid:
                left = mid+1
            else:
                right = mid
        return right


class Solution:
    """
    Approach 2: Bit Manipulation
    time: O(nlogn), space: O(1)
    Requirement: space: O(1)
    """
    def findDuplicate(self, nums: List[int]) -> int:



class Solution:
    """
    Approach 3: Fast-slow Pointers (Floyd's cycle-finding algorithm)
    time: O(n), space: O(1)
    related: 141. Linked List Cycle
    Requirement: space: O(1)
    Follow-up requirement: time: O(n)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow_2 = 0
        while slow != fast:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        return slow
