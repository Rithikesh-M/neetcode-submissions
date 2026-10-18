class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1 
            else:
                count[num] += 1 
        for val in count.values():
            if val > 1:
                return True 
        return False 
 
            
        