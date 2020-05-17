class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m,n=len(s),len(p)
        if n==0 or m==0 or n>m:
            return []
        cs=[0]*26
        ct=[0]*26
        for i in range(n):
            ct[ord(s[i])-97]+=1
            cs[ord(p[i])-97]+=1
        #print(cs,ct)
        def com(a,b):
            for i in range(len(a)):
                if(a[i]!=b[i]):
                    return False
            return True
        ans=[]
        for i in range(n,m):
            #print(cs,ct)
            if com(cs,ct):
                ans+=[i-n]
            ct[ord(s[i])-97]+=1
            ct[ord(s[i-n])-97]-=1
        if com(cs,ct):
            ans+=[m-n]
        return ans
