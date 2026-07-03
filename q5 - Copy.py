#print the table of 2 like 
# 2 * 1 = 2
# 2 * 2 = 4
x=int(input("enter whose table you wnat to print:"))
for i in range(1,11,1):
    print("{} * {} = {}".format(x,i,(x*i)))