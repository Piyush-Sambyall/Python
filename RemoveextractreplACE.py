u1=[425,78,54,["hello","There",["aman","Rohit",78],"ARE","class"],145,223,200]
#q1 remove 200 from the list
#q2 replace 2nd 78 with 500
#q3 extract "There",["aman","Rohit",78],"ARE","class"
#q4 replace "hello","There" with "bye","bye"

#ans 1
u1.pop(-1)
print(u1)

#ans 2
u1[3][2][2]=500
print(u1)

#ans 3
print(u1[3][1:])
print(u1)
#ans 4
u1[3][0]=u1[3][0].replace("hello","bye")
u1[3][1]=u1[3][1].replace("There","bye")
print(u1)
