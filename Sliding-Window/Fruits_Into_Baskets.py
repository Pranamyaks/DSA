class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        freq={}
        maxlen=0

        for right in range(len(fruits)):
            if fruits[right] in freq:
                freq[fruits[right]]+=1
            else:
                freq[fruits[right]]=1

            while len(freq)>2:
                freq[fruits[left]]-=1

                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1

            maxlen=max(maxlen,right-left+1)
        return maxlen                    
        
