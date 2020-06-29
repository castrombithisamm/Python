fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)
di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
#print(di)

#find the most common word
largest = -1
theword = None
for k,v in di.items():
     print(k,v)
     if v > largest:
         largest = v
         theword = k #capture/remember the key that was largest
print ('Largest',theword, largest)
