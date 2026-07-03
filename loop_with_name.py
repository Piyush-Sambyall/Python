name=["abhiniza","pankaj","robin","amit","archana","aastha","rajneesh","apoorv"]


# print those names which start with "a"
for i in name:
    if(i.startswith("a")):
        print(i)
print("")

for i in name:
    if(i[0]=="a"):
        print(i)
print("")
#print those names which start with "a" and ends with "t"
for i in name:
    if(i[0]=="a" and i[-1]=="t"):
        print(i)
print("")
# print those name where letter is more than 6
for i in name:
    if(len(i)>6):
        print(i)
print("")
#print starting 4 letters of all the names
for i in name:
    print(i[:4])
