class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d={}
        for i in S:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=0
        for j in J:
            if j in d:
                ans+=d[j]
        return ans
