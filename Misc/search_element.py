'''li=[1,6,3,5,3,4]
search=int(input("Enter the elements to be searched:"))
if search in li:
    print("Element found")
else:
    print("Element not found")
  '''  
'''
li=[20,100,20,1,10]
small=li[0]
large=li[0]
for i in li:
    if i <small:
        small=i
        print("Small num is",small)
    if i >large:
        large=i
        print("Large num is",large)

'''
'''
n=[70,11,20,4,100]
first_large=n[0]
sec_large=n[0]
for i in n:
    if i > first_large:
        sec_large=first_large
        first_large=i


print(sec_large)
'''
str="welcome to python programming"
n=str.split()
rev=n[::-1]
op=" ".join(rev)
print(op)
