class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d=[0 for i in range(N)]
        for i in range(len(trust)):
            d[trust[i][0]-1]-=1
            d[trust[i][1]-1]+=1
        for i in range(len(d)):
            if d[i]==N-1:
                return i+1
        return -1
