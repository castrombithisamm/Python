fhand = open('Django.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('a'):
        continue
    print(line)