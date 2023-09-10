class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j]==target:
                    return [i, j]
            

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for idx, n in enumerate(nums):
            diff_dict[n] = idx
        
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in diff_dict and diff_dict[diff]!=idx:
                return [idx, diff_dict[diff]]
