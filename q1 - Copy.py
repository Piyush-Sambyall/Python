# print elements between 10 and 20
l=[10,15,14,26,23,20,25,21,15,17,18,14]
for i in l:
    if(i>10 and i<20):
        print(i)
print("")
#print all even elements
for i in l:
    if(i%2==0):
        print(i)
#print square of even elements
print("")
for i in l:
    if(i%2==0):
        print("square of {} is {}".format(i,i**2))

print("")
#print those elements which is more than average of list
average=sum(l)//len(l)
for i in l:
    if(i>average):
        print(i)
print("")
#print those elements which are perfect square
li=[4,9,16,25,2,3,4,5,6,7]
for i in li:
    if(i**(1/2)==int(i**(1/2))):
        print(i)