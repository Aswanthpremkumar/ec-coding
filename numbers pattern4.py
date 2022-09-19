a=1
for k in range(6):
    print(" *",end=" ")
    if k==1 or k==5:
        print(a,end=" *")
    elif k==2 or k==4:
          print(a,"*",a+1,"*",a,end=" *")
    elif k==3:
          print(a,"*",a+1,"*",a+2,"*",a+1,"*",a,end=" *")
    print("")
print(" *")


 
