fhand = open('Django.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('a'):
        print(line)