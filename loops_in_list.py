a=[10,20,30,40,50]
for b in a: #b becomes a[b] in loop
    print(b)

print(type(b))

#print those elements which are more than 30
for b in a:
    if(b>30):
        print(b)
print("")
#print the square of all elements of the list
for b in a:
    print(b**(2))
print("or")
for b in a:
    print("{} is the square of {}".format((b**(2)),b))

#print the square of elements greater than 20
s=[7,4,8,6,3,2,1,5,4,7]
for i in s:
    if(i>6):
        print(i**2)
