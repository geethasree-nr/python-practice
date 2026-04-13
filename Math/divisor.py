n = int(input("Enter a number: "))

factors = []

for i in range(1, n+1):
    if n % i == 0:
        factors.append(i)

print("The divisors of", n, "are:", ", ".join(map(str, factors)))