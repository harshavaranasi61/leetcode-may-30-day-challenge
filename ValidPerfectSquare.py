import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(int(math.sqrt(num))==math.sqrt(num)):
            return True
        return False
