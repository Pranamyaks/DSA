class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen={0:-1}
        prefix=0

        for i in range(len(nums)):
            prefix+=nums[i]

            if k!=0:
                remainder=prefix%k
            else:
                remainder=k

            if remainder in seen:
                if i-seen[remainder]>=2:
                    return True
            else:
                seen[remainder]=i

        return False                        
        
