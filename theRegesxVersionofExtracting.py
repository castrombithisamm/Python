import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)' ,lin)
print(y)

#OR
y = re.findall('^From .*@([^ ]*)' ,lin)
print(y)


