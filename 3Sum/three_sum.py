#O(n^2), space: O(n), using 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        vals = {}
        if len(nums)<3: return []
        nums.sort()
        k=0
        while k>=0 and k<len(nums) and nums[k]==0:
            k+=1

        if k>=3:
            nums = nums[k-3:]
        
        for i in range(len(nums)):
            vals[nums[i]] = i
        
        
        solutions = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = 0 - nums[i] - nums[j]
                if diff in vals and i!=vals[diff] and j!=vals[diff]:
                    cont = [nums[i],nums[j], diff]
                    min_idx = cont.index(min(cont))
                    min_ = cont[min_idx]
                    cont.pop(min_idx)
                    max_idx = cont.index(max(cont))
                    max_ = cont[max_idx]
                    cont.pop(max_idx)
                    soln = '|'.join([str(min_),str(cont[0]),str(max_)])
                    solutions.add(soln)
        
        res = []
        for soln in solutions:
            res.append(soln.split('|'))
        return res


#O(n^2), iterating over the list and using two pointers over the rest of the list
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1; r-=1
        return res
                    