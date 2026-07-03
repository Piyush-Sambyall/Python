#set is an unordered collection of unique elements which does not contain duplicate elements and it is mutable
# note:- no indexing and slicing

s=set()
print(type(set()))

r={1,5,6,8,3,1,0,3,8,0,3,76,5} #set banane ke liye curly braces
print(r)

print(r.pop()) #it removes random elements from the list

q1={1,2,3,4,5,6,7,800,900,500}
q2={11,22,33,4,5,6,7,902,501,802}

print(q1.intersection(q2)) #prints common value from both the sets

print(q1.difference(q2)) #prints unique elements from left set

print(q1.symmetric_difference(q2)) #prints unique elements from both sets

print(q1.union(q2)) #it combines 2 set in single set-> isme common wale bhi aa rahe hai

q1.remove(5) #delete given element from the set 
print(q1)

q1.update(q2) #it will add all elements of right set into left set
print(q1)

