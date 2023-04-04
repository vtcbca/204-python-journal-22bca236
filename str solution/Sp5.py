def symmetric(lis):
    h=(len(lis)//2)
    f=lis[:h]
    s=lis[h:]
    if f==s:
        print(f"String {} is symmetric!!!!".format(lis))
    else:
        print("String {} is not symmetric!!!".format(lis))



a=input("Enter a string:")
symmetric(a)
          