class Solution:
    def findComplement(self, num: int) -> int:
        if(num == 0):
            return 1
        i=1
        while i <= num:
            i = i << 1
        return (i-1)^num