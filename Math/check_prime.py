class prime:
    def check_prime(self,n):
        count=0
        if n<1:
            print(f"{n} is not a prime number")
        else:
            for i in range(1,n+1):
                if n%i==0:
                    count+=1
            if count == 2:
                print(f"{n} is a prime number")
            else:
                print(f"{n} is not a prime number")
        
p=prime()
n=int(input("Enter the Number:"))
p.check_prime(n)



class sums:
    def problems(self,n):
        sum=0
        while(n>0):
            rem=n%10
            sum+=rem
            n=n//10
        print(sum)

s=sums()
n=int(input("Enter the num:"))
s.problems(n)
