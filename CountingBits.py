class Solution:
    def countBits(self, num: int) -> List[int]:
        ans=[0,1,1,2,1,2,2,3]
        d=[1,2,2,3]
        i=len(ans)
        j=3
        f=4
        if(num<=7):
            return ans[:num+1]
        flag=0
        while(i<=num):
            #print(i,j)
            if ans[-1]==j:
                flag=1
                c=0
                f=2*f
                j+=1
            if flag==0:
                ans.append(ans[i-f]+1)
                i+=1
            elif flag==1:
                ans.append(d[c])
                c+=1
                i+=1
                if(c==4):
                    flag=0
        return ans
