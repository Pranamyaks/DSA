class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k        

        
