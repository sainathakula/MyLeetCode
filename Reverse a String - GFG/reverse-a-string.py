#User function Template for python3

def reverseWord(s):
    #your code here
    lis=list(s)
    start=0
    end=len(lis)-1
    while(start<end):
        lis[start],lis[end]=lis[end],lis[start]
        start+=1
        end-=1
        
    z = "".join(lis)
    return z

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends