def makedict(lis):
    di={}
    c=int(input("Enter minimum word length:"))
    for i in lis:
        if len(i)>=c:
            di[i]=len(i)

    print(di)

def input1():
    str=input("Enter sentence:")
    m=str.split(" ")
    makedict(m)

input1()    