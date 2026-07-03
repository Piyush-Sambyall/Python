w=[4,7,9,6,4,2,3,1,0,2,3]

# prints the maximum element
print(max(w))

# prints the minimum element
print(min(w))

# prints the total or sum of the list
print(sum(w))

# prints number of elements
print(len(w))

# inbuit function of string:

# prints the count of given element
print(w.count(2))

# it will add an element in the end of the string
w.append(500)
print(w)

# it prints and removes the last element of the list
w.pop()
print(w)

# pop can also remove value from any specified index

w.pop(0)
print(w) #-> 4 is removed

# add more than 1 element at the end of the list
w.extend([200,400,600])
print(w)

# removes the given element 
w.remove(2)
print(w)

# it will add an element on the given index and push the last element
# syntax-> list.insert(index,value)
w.insert(1,88)
print(w)

# prints the index value of given element
print(w.index(200))

print(w.index(2,5)) #to find index of repeating numbers

# it will reverse the list
w.reverse()
print(w)

#it will sort the list in ascending order
w.sort()
print(w)

#it will sort the list in descending order
w.sort(reverse=True)
print(w)

# makes a copy of the list
n_list=w.copy()
print(n_list)

#it removes all the elements and make a blank list
w.clear()
print(w)