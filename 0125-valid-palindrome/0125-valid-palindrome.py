class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=""
        for i in s:
            if(i.isalnum()):
                d+=i.lower()
            
        g=d[::-1]
        print(d)
        print(g)

        if(g==d):
            return True
        else:
            return False