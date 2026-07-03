st="""Each row contains a unique village, the block containing the village and 
the district containing the block. Since village name may not be unique, the field
village_code is used as the unique identifier for each village.
Primary key: village_code child_register Contains the information of th"""

#1-> convert whole string to uppercase

print(st.upper())

#2-> find the index value of 2nd  "village"

print(st.find("village",28))

#3-> remove the "unique identifier for each village"

print(st.find("unique",140))
print(st.find("village",211))

print(st[:185], st[220:])

#4-> print the count of "village"

print(st.count("village"))

#5->split whole string using "block"
print(st.split("block"))

#6-> extract "Since village name may not be unique" from string

print(st.find("Since"))
print(st.find("unique",21))

print(st[109:145])

#7-> replace "Since village name may not be unique" with "Since city name may not be unique"

print(st.replace("Since village name may not be unique","Since city name may not be unique"))

#8-> extract "Primary key: village_code" but output must be in uppercase

print(st.find("Primary"))
print(st.find("code",166))

print(st[221:246].upper())