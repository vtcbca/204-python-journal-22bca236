def evenodd(l):
    e1[]
    e2=[]
    n1=0
    n2=0
    for i in l:
        if i%2==0:
            e1.append(i)
            n1+=1
        else:
            e2.append(i)
            n2+=1
    
    print(f"The even numbers are {n1} and numbers:")
    for i in e1:
        print(i)
-
    print(f"The odd numbers are {n2} and numbers:")
    for i in e2:
        print(i)

def createlist()
    li=[]
    a=int(input("How many numbers you want to enter in list:"))
    for i in range(a):
        c=int(input("Enter a number:"))
        li.append(c)
    evenodd(li)

createlist()