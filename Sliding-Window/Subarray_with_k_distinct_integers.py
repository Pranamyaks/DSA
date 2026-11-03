class Solution(object):
    def subarraysWithKDistinct(self, nums, k):

        def atMost(k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            left=0
            freq={}
            count=0

            for right in range(len(nums)):
                if nums[right] in freq:
                    freq[nums[right]]+=1
                else:
                    freq[nums[right]]=1

                while len(freq)>k:
                    freq[nums[left]]-=1

                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left+=1    
                count+=right-left+1
            return count
        return atMost(k)-atMost(k-1)                   
            
