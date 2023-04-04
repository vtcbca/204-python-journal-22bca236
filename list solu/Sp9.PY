def dicto(list1):
    dics={}
    for i in range(0,len(list1),3):
        dic[list1[i]]=list1[i+1:i+3]

    print(dics)
def takeinput():
    m=[]
    i="y"
    while i=="y" or i=="Y":
        b1=int(input("Student id:"))
        m.append(b1)
        b2=input("Student name:")
        m.append(b2)
        b3=float(input("Student percentage:"))
        m.append(b3)
        i=input("Do you add more ?(y/Y):")
    print(m)
    dicto(m)

takeinput()