class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if(len(coordinates)==2):
            return True
        if coordinates[1][0]-coordinates[0][0]==0:
            m=0
        else:
            m=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        for i in range(2,len(coordinates)):
            if((coordinates[i][1]-coordinates[0][1])==(m*(coordinates[i][0]-coordinates[0][0]))):
                continue
            else:
                return False
        return True
