num =0
tot =0.0
while True:
    sval = input('Enter a anumber: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print ('invalit input')
        continue
    print(fval)
    num = num +1
    tot = tot+ fval
print('All done')
print(tot,num,tot/num)