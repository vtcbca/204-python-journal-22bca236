#python script to check string is palindrome or not
a=input("Enter string :")
b=a[::-1]
if(a==b):
    print(f"String {a} is palindrome !")
else:
    print(f"String {a} is not palindrome !")
