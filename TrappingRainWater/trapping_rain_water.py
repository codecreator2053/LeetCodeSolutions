# O(n^2)
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(height)-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])
            ans += max((min(right_max, left_max) - height[i]), 0)
        return ans

#O(n), space_complexity: O(n)
class Solution2:
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        cur_max = 0
        l_max = []
        for i in range(len(height)):
            cur_max = max(cur_max, height[i])
            l_max.append(cur_max)
        cur_max = 0
        r_max = []
        for i in range(len(height)-1, -1, -1):
            cur_max = max(cur_max, height[i])
            r_max.append(cur_max)
        r_max = r_max[::-1]
        
        for i in range(len(height)-1):
            ans += max((min(r_max[i], l_max[i]) - height[i]), 0)
        return ans