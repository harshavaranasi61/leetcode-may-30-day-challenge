class Solution:
    def findComplement(self, num: int) -> int:
        b=""
        while(num>0):
            b+=str(num%2)
            num=num//2
        print(b)
        b=list(b[::-1])
        for i in range(len(b)):
            if(b[i]=='1'):
                b[i]='0'
            else:
                b[i]='1'
        print(b)
        ans=0
        i=0
        while(i<len(b)):
            ans+=(int(b[-1-i])*(2**i))
            i+=1
        return ans
