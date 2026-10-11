class Solution(object):
    def majorityElement(self, nums):
        count=0
        candidate=0
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1 
        return candidate             
        
