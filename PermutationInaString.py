class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        if n==0 or m==0 or m>n:
            return False
        cs=[0]*26
        ct=[0]*26
        for i in range(m):
            ct[ord(s1[i])-97]+=1
            cs[ord(s2[i])-97]+=1
        print(cs,ct)
        def com(a,b):
            for i in range(len(a)):
                if(a[i]!=b[i]):
                    return False
            return True
        ans=[]
        for i in range(m,n):
           # print(cs,ct)
            if com(cs,ct):
                return True
            cs[ord(s2[i])-97]+=1
            cs[ord(s2[i-m])-97]-=1
        if com(cs,ct):
            return True
        return False
