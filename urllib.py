
import urllib3.request, urllib3.parse, urllib3.error
fhand = urllib3.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in  fhand:
    print(line.decode().strip())
    