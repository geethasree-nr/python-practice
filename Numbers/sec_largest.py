a=[12,35,1,10,34,1]
first_large=-1
second_large=-1
for i in a:
    if i > first_large:
        second_large=first_large
        first_large=i
    elif i > second_large:
        second_large=i
print(f"The Second large {a} number =",second_large)
