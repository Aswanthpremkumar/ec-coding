h=5
for x in range(h):
    if x in (0,2,4):
        print(" "*(h-x),"*"*(2*x + 1))
    else:
        print(" "*(h-x),"-"*(2*x + 1))
for x in range(h - 2, -1, -1):
    if x in (0,2):
     print(" " * (h - x), "*" * (2*x + 1))
    else:
        print(" "*(h-x),"-"*(2*x + 1))
