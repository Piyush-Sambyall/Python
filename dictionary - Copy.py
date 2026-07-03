#dictionary- it is a pair of key and values
d={}
print(type(d))

d={"name":["A","B","C","D"],"ID":[1001,1002,1003,1004]} #it has pair of name(keys) and values
print(d)

# prints the name of all keys of dictionary

print(d.keys())

# prints the values of dictionary
print(d.values())

d["name"][0]="X"
d["name"][1]="Y"

