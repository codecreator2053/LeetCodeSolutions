#time complexity: O(n)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        
        return i


class Solution2:
	def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:return 0
        if len(nums)==1: return 0 if nums[0]==val else 1
        l = 0
        r = len(nums)
        while l<r:
            if nums[l] == val:
                nums[l] = nums[r-1]
                r -= 1
            else:
                l += 1
            print(l, r)
        return r