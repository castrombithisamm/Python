fhand = open('Django.txt')
for line in fhand:
    line = line.rstrip()
    if not 'superclass' in line :
        continue
    print(line)