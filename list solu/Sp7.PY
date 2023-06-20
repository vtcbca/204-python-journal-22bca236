
def changename(li):
    filename=[]
    a=".c"
    for i in li:
        if a in i: 
            b=i.replace(".c",".py")
            filename.append(b)
        else:
            filename.append(i)    

    print(filename)    

fi = ["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
changename(fi)
