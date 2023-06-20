#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
a=input("Enter sentece:")
b=sr.split(" ")
c=0
d=[]
for i in b:
    if (i==i[::-1]):
        c=c+1
        d.append(i)
if c>0:
    print('The number of palindrome word in sentence is {} and palindrome words are:{}.'.format(c,d))              
else:
    print("There are no palindrome word in sentence!!!")    

   