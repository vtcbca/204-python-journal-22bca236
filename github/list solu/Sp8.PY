def change(lis):
    n=[]
    b1=int(input("Enter value you want to replace:"))
    c1=int(input("Enter value you want to change with:"))
    for i in lis:
        if b1==i:
            n.append(c1)
        else:
            n.append(i)    
    print(n)

def createlist():
    li=[]
    b=int(input("How many numbers you want to enter in list:"))
    for i in range(b):
        c=int(input("Enter a number:"))
        a.append(c)
    change(li)

createlist()