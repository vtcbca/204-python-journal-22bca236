def conseecoomon(li):
    c=0
    b=[]
    for i in range(len(li)-2):
        if li[i]=li[i+1] and li[i+1]==li[i+2]:
            b.append(li[i])
            c+=1
    if c>0:
        print(f"Consecutive common numbers are {c} as follow:{b}")
    else:
        printf("No consecutive number!!")
def takeinp():
    n=[]
    b=int(input("How many number you want to enter in list:"))
    for i in range(b):
  
        c=int(input("Enter value:"))
        n.append(c)
    consecoomon(n)        

takeinp()    
