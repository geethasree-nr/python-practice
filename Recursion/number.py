def print_numbers(n):
    if n==0:
        return 
    else:
        print_numbers(n-1)
        print(n)
        
print_numbers(5)
