#create two list and add perfect square in square list and add perfect cube in cube list 
import math
l=[4,9,16,25,36,49,81,27,8,512]
square=[]
cube=[]
for i in l:
    if (i**(1/2)==int(i**(1/2))):
        square.append(i)
    if math.cbrt(i)==int(math.cbrt(i)):
        cube.append(i)

print(square)
print(cube)

# print 2nd highest element from the list

l=[4,9,16,25,36,49,81,27,8,512,512,512,78,89]
l.sort()
# index=-2
# for i in l:
#     if l[index]==max(l):
#         index-=1
# print(l[index])

m=max(l)
for i in l:
    if(i!=m):
        sm=i
print(sm)

