# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

modnu=10**9+7
def nchoosek(n,k):
    global modnu
    if n < k:
        return 0
    elif k==0:
        return 1
    else:
        t=1
        u=max(k,n-k)
        for i in range(1,min(k,n-k)+1):
            t=(t*(u+i)/i)%modnu
        return t
                                

                                            
def foxsequence(n,m):     
    global modnu
    if m==1:
        return 1
    fox_se=0

    for k in range(int(math.ceil(n/float(m))),n+1):       
        t=0                    
        for r in range(m):                
            if m+n-2-k-k*r>=m-2:                    
                t=t+((-1)**(r%2))*nchoosek(m-1,r)*nchoosek(m+n-2-k-k*r,m-2)                
            else:
                break                                          
        fox_se=(fox_se+t)%modnu
         
    return (fox_se*m)%modnu
             
n=input()


for i in range(n):                               
    t=map(int, raw_input().split())    
    print foxsequence(t[0],t[2]-t[1]+1)

