t1=(1,2,3)
t2=(2,1,3)
print(t1+t2)
print(t1*2)
print(1 in t1)
print(5 in t1)
print(len(t1))
print(max(t1))
print(min(t1))

t3=(t1,t2)
print(t3)

tuple=(0,1,2,3)
print(tuple[1:])
print(tuple[::-1])
print(tuple[2:4])
#SETS
set1={1,2,3}
set2={3,2,1}
print(set1==set2)

#duplicte values
set1={1,2,3,4,4}
print(set1)

#adding
s1=set(["a","b","c"])
print(s1)
s1.add("d")
print (s1)


#set union
a={'a','b','c','d'}
b={'d','e','f'}
c={'g','h','f'}
x=a.union(b).union(c)
print(x)
y=a|b|c
print(y)

#set intersection
a={'a','b','c'}
b={'c','e','f'}
x=a.intersection(b)
print(x)
y=a&b
print(y)

#set difference
a={'a','b','c'}
b={'c','e','f'}
x=a.difference(b)
print(x)
y=a-b
print(y)

#deleting all values
set1={1,2,3,4,5,6}
print("initial set")
print(set1)
set1.clear()
print("set after using clear() function")
print(set1)

#symmetric difference
a={'a','b','c'}
b={'c','e','f'}
x=a^b
print(x)

#length of set
a={'a','b','c'}
print(len(a))

#maximum and minimum
a={'a','b','c'}
print(max(a))
print(min(a))


