#total = 0
#count = 0
#while True :
 #   inp = input('Enter a number: ')
  #  if inp == 'done' : break
   #3 value = float(inp)
    #total = total + value
    #count = count + 1
#average = total / count
#print('Average: ', average)

    #OR
     
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average: ', average)