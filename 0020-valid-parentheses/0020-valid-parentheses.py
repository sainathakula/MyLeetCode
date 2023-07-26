class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if(len(s)==1):
            return False
        else:
            for i in range(len(s)):
                if(s[i]=='(' or  s[i]=='{' or s[i]=='[' ):
                    stack.append(s[i])
                else:
                    if len(stack)== 0:
                        return False
                    if((s[i]==')' and stack[-1]=='(' ) or (s[i]=='}' and stack[-1]=='{' ) or (s[i]==']' and stack[-1]=='[' )):
                        stack.pop()
                    else:
                        return False
                        # pass
        if len(stack)==0:
            return True
        else:
            return False
        
        