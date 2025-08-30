class Solution(object):
    def reverse(self, x):
        
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
           x = x * -1
           x = int("".join(reversed(str(x)))) * -1
        else:
           x = int("".join(reversed(str(x))))
        if x < -2**31 or x > 2**31 - 1:
            x=0   
        return x    


           