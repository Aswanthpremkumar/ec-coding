a=0
for k in range(5):
    for l in range(k):
        a+=1
        print(a,end="*")
    print("")
b=6
for i in range(4,0,-1):
    for j in range(i):
        b=b+1
        if b==0:
            b=2
            print(b,end="*")
        elif b==1:
            b=3
            print(b,end="*")
        elif b==-3:
            b=1
            print(b,end="*")
        else:
         print(b,end="*")
    b=b-7
    print("")
    
