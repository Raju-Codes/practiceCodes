#REGEX
import re

#re.search it searches data from pattern and with the string given.
print(re.search("abc","abcde"))

#re.match
print(re.match("abc","acde abc"))

# re.findall()
text= "Hi i was abc and with new name abc, age 14 born year 1998"
print(re.findall("abc",text))

#re.sub()
print(re.sub("abc","Rajesh",text))

#re.findall(r"\d+", text) to search digits inside the text.
print(re.findall(r"\d+",text))