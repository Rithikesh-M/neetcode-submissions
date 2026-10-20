class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(node):
            if node >= len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[node])
            dfs(node + 1)
            subset.pop()
            dfs(node + 1)
        dfs(0)
        return res