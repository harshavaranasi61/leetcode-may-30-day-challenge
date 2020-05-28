from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        l=[]
        for i in c:
            l.append([i,c[i]])
        l=sorted(l,key=lambda x:x[-1],reverse=True)
        return "".join(i[0]*i[1] for i in l)
