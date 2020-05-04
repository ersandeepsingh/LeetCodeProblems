class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        jwel = [i for i in J]
        print (jwel)
        for i in S:
            if(i in jwel):
                count +=1
                print(i,count)
        return count
        