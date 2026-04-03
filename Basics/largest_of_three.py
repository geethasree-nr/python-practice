a=int(input("Enter a number A:"))
b=int(input("Enter a number B:"))
c=int(input("Enter a number C:"))

if (a>=b and a>=c):
    print("A is greater")
elif(b>=a and b>=c):
    print("B is greater")
else:
    print("C is greater")
