class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        count = []

        def dfs(node, curr, total):
            if total == target:
                count.append(curr.copy())
                return 
            if node >= len(nums) or total > target:
                return 
            curr.append(nums[node])
            dfs(node, curr, total + nums[node])
            curr.pop()
            dfs(node + 1, curr, total)
        dfs(0, [], 0)
        return count 



        