k=[1,4,7,6,3,5,[88,99,22,10],4,"string",8,5]


print(k[4:9])

#print 99
print(k[6][1])

#replace [88,99,22,10] by 5
k[-5]=5
print(k)

#print ring of string

k[-3]=k[-3].replace("i","a")
print(k)

# replace string b any number and find the average of list
k.pop(-3)
print(k)
k.insert(-2,10)
print(k)

print((sum(k)/len(k)))