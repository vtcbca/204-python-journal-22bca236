#write a script to create a list with 5 string and count total number of length with string using UDF.
def evenstr(a):
    s=[]
    c=0
    for i in a:
        if(len(i)%2==0):
            s.append(i)
            count=count+1
    if(count>0):
        print('The number of even string is {} and string :{}'.format(c,s))
    else:
        print("No even string available!")

lis=[]
for i in range(5):
    b=input("Enter string:{}:".format(i+1))
    lis.append(b)    
evenstr(lis)    