import re
with open("data.txt","r") as f:
    filestr = f.read()

Names = re.findall(re.compile("(^[A-Z][a-z]+\s)([A-Z][a-z]+)"),filestr)
Address = re.findall(re.compile("([0-9]+\s)([A-Z][a-z]+\s[A-Za-z\.\,\s]+)([0-9]+)"),filestr)
MobileNo =  re.findall(re.compile("(\d{3}\-)(\d{3}\-)(\d{4})"),filestr)
replaced = re.sub("Dave","John",filestr)

for x in Names:
    print(x[0]+x[1])

for x in Address:
    print(x[0]+x[1]+x[2])

for x in MobileNo:
    print(x[0]+x[1]+x[2])

print(replaced)
