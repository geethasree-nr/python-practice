n=int(input("Enter the number:"))
print("Before reversing the number:",n)
rev=0
while (n>0):
    rem=n%10
    rev=rev*10 +rem
    n=n//10
print("After reversing the number:",rev)


