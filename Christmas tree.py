a=int(input("enter number of lines in triangle:"))
b=int(input("enter number of colums in base:"))
c=int(input("enter a divided by 2(eg:3/2=1):"))
def triangle(a):
    for i in range(1,a+1):
        print(' '*a, end='')
        print('* '*(i))
        a-=1
triangle(a)
triangle(a)
triangle(a)
def base(b):
    print(' '*c,end='')
    print(' *'*b)
base(b)
base(b)
base(b)
