class Solution:
    """
    Approach 1: two pointers
    time: O(n), space: O(1)
    """
    def reverseString(self, s: List[str]) -> None:

        """
        Do not return anything, modify s in-place instead.
        """

        p1, p2 = 0, len(s)-1
        while p1 <= p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1

        # alternative code: Slicing  s[:] = s[::-1]
