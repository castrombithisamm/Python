fh = open('mbox-short.txt')
print(fh)

for line in fh:
    ly = line.rstrip()
    print(ly.upper())