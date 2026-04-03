p=float(input("Enter the principal:"))
r=float(input("Enter the Rate:"))
t=float(input("Enter the Time:"))

a=p*(1+r/100)**t
CI=a-p
print("Compound Intrest=",round(CI,2))
