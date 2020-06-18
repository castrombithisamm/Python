num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    #print(fval)
    num = num+1
    tot = tot+fval
    #print('All Done')
    print(num, tot, tot/num)
