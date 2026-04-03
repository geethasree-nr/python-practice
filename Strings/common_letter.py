def common_letter():
    str1=input("Enter the Name_1:").lower()
    str2=input("Enter the Name_2:").lower()
    s1=set(str1)
    s2=set(str2)
    same=s1& s2
    print(f"The common letterns in two strings is",same)
common_letter()
