def check_prime(n):
    count=0
    if n <1:
        print(f"{n} is not a prime number")
    else:
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")


n=int(input("Enter the number to check prime or not:"))
check_prime(n)
