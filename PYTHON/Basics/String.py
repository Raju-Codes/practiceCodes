s1 = """Hello """
print(len(s1))
#Indexing in Python
s2 = "python world"
print(len(s2))
print(s2[1],s2[-1])
print(s1+s2)

# To find the length of a string
print(len(s1), "length of the string")

# To get single char with index number
print("single letter",s2[1],"last character",s2[-1])

# to print each letter in loop
for i in s2:
    print(i)

# Operation in Strings
# Slicing String
print(s2[1:4:2])
