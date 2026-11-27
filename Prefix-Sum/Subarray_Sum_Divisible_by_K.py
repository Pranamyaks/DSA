class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix=0
        count=0

        remainder_count={0:1}

        for num in nums:
            prefix+=num

            remainder=prefix % k

            if remainder in remainder_count:
                count+=remainder_count[remainder]

            remainder_count[remainder]=remainder_count.get(remainder,0)+1

        return count            
        
