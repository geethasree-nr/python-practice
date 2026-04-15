def print_number(n):
    if n==0:
        return
    else:
        print(n)
        print_number(n-1)
print_number(5)