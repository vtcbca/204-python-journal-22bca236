#write a listb of menudriven 
a=[]
q="y"
while q=="y" or q=="Y":

  print("\n1.Add iteams in list.\n2.print string with even character in length.\n3.Replace odd character of string with index no.\n4.enter start and end value and extraxt character from the string\n")
  c=int(input("Enter your choice!!"))

  if c==1:
          a1="y"
          while a1=="y" or a1=="Y":
            i=input("Enter a string you want to enter:")
            a.append(i)
            a1=input("do you add more string press (y/Y):")
               
  elif c==2:
          b=[]
          count=0
          for i in a:
            if(len(i)%2==0):
              b.append(i)
              count+=1
          if count>0:    
            print(f"Strings with even character is {b}")  
          else:  
            print("String has no even charcater in it.....")     
  elif c==3:
          p=[]
          for i in a:
              o=[]   
              for enu,j in enumerate(i):
                if enu%2==0:
                  o.append(enu)
                else:
                  o.append(j)
              p.append(o) 
          for i in p:
            print(i)    

  elif c==4:
          s=int(input("Enter start index:"))
          e=int(input("Enter end index:"))
          res=" ".join([sub for sub in a ])[s:e]
          print(f"Your string is {res}")          

  q=input("Do youy want to continue:(y/Y):")        