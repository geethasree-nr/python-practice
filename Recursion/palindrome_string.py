class Solution:    
    def palindromeCheck(self, s):
        rev=s[::-1]
        if s==rev:
            return True
        else:
            return False
s=input()
obj=Solution()
print(obj.palindromeCheck(s))