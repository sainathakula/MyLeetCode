class Solution:
    def findSum(self,A,N): 
        #code here
        if (N%2==0):
            mx=A[1]
            mn=A[0]
            i=2
        else:
            mx=mn=A[0]
            i=1
        while(i<n-1):
            if(A[i]<A[i+1]):
                mx=max(mx,A[i+1])
                mn=min(mn,A[i])
            else:
                mx=max(mx,A[i])
                mn=min(mn,A[i+1])
            i=i+2
        return mx+mn



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends