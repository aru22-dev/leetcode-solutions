import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ogstr=re.sub(r'[^a-zA-Z0-9]','',s).lower().replace(" ", "")
        if ogstr == "".join(reversed(ogstr)):
           return True
        else:
           return False
           
           
           
        
        
        return True