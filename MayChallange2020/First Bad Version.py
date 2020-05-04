# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #if(isBadVersion(n) is False):
         #   return n
        left,right=1,n
        if(n == 1):
            return 1
        while(left < right):
            mid = (left + right)//2
            if(isBadVersion(mid)):
                right = mid 
            else:
                left = mid + 1
            
            print(left, right, mid)
        
        return left
            
                
        
        