
def changename(li):
    filename=[]
    a=".c"
    for i in li:
        if a in i: 
            b=i.replace(".c",".py")
            filechange.append(b)
        else:
            filechange.append(i)    

    print(filename)    

fi = ["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
changename(fi)