class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h=[0 for i in range(26)]
        for i in range(len(ransomNote)):
            h[ord(ransomNote[i])-97]+=1
        h1=[0 for i in range(26)]
        for i in range(len(magazine)):
            h1[ord(magazine[i])-97]+=1
        for i in range(26):
            if(h1[i]>=h[i]):
                continue
            else:
                return False
        return True
