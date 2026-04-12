n=4
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i+1):
        print(i-j+1,end=" ")
        
    print()