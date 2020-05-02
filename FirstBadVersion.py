# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        return self.binary(0,n)
    def binary(self,l,r):
        while(l<r):
            mid=(l+r)//2
            if(isBadVersion(mid)==False):
                l=mid+1
            else:
                r=mid
        return l
