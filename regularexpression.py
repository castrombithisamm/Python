import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('From: ', line):
     #   print(line)

# re.search() can also be used like the startswith() function
    if re.search('^From: ', line):
        print(line)