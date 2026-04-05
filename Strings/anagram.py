def check_anagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("Anagram")
    else:
        print("Not anagram")
s1=input("Enter the first string:")
s2=input("Enter the second string:")
check_anagram(s1,s2)
