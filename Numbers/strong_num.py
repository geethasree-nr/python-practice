n=int(input("Enter the number:"))
temp=n
strong=0
while(n>0):
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    strong=strong+fact
    n=n//10
if(temp==strong):
    print("it is a strong number")
else:
    print("Not a strong number")
    
    
