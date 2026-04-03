def palindrome():
    str=input("Enter the String:").lower()
    rev=str[::-1]
    if (str==rev):
        print(f" {str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")
palindrome()
