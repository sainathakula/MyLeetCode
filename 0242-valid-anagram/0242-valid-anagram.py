class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==len(t)):
            ss=list(s)
            tt=list(t)
            ss.sort()
            tt.sort()
            if(ss==tt):
                return True
        else:
            return False