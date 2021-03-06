class Solution(object):
    def rob_help(self, nums):
        withSelf = withoutSelf = 0
        for n in nums:
            withSelf, withoutSelf = withoutSelf+n, max(withSelf, withoutSelf)
        return max(withSelf, withoutSelf)    
    def rob(self, nums):
        return max(nums[0] + self.rob_help(nums[2:-1]), self.rob_help(nums[1:])) if len(nums) else 0
