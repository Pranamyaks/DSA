class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum=0
        hashmap={0:1}
        count=0

        for num in nums:
            prefix_sum+=num
            remaining=prefix_sum-k

            if remaining in hashmap:
                count+=hashmap[remaining]

            hashmap[prefix_sum]=hashmap.get(prefix_sum,0)+1
            
        return count        
        
