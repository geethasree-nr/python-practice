num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
small=max(num1,num2)
for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print("The GCD of",num1,"and",num2,"is",gcd)