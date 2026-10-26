class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        window_sum=0
        max_sum=0
        left=0
        seen=set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                window_sum-=nums[left]
                left+=1
            seen.add(nums[right])
            window_sum+=nums[right]

            if right-left+1>k:
                seen.remove(nums[left])
                window_sum-=nums[left]
                left+=1
            if right-left+1==k:
                max_sum=max(window_sum,max_sum)
        return max_sum                
        
