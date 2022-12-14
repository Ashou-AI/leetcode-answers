class Solution:
    """
    Approach 1: Monotonic Stack
    time: O(n), space: O(n)
    """
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # pair: [num_1, num_3]
        num_1 = nums[0]
        for num_2 in nums[1:]:
            while stack and num_2 >= stack[-1][1]:
                stack.pop()
            if stack and num_2 > stack[-1][0]:
                return True
            stack.append([num_1, num_2])  # new: [num_1, num_3]
            num_1 = min(num_1, num_2)
        return False


class Solution:
    """
    Approach 1.2: Monotonic Stack (alternative code)
    time: O(n), space: O(n)
    """
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # the stack of num_2
        num_3 = -(10 ** 9 + 7)
        for num_1 in nums[::-1]:
            while stack and num_1 > stack[-1]:
                num_3 = max(num_3, stack.pop())
            if stack and num_1 < num_3:
                return True
            stack.append(num_1)  # append num_2
        return False
