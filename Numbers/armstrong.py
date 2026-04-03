n=int(input("Enter the number:"))
temp=n
arm=0
while(n>0):
    rem=n%10
    arm=arm+rem**3
    n=n//10
if(temp==arm):
    print("Armstrong Number")
else:
    print("Not a armstrong number")
