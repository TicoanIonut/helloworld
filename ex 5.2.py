smallest = None
largest = None
num = 0
tot = 0.0
while True:
    sval = input("enter a number")
    if sval == 'done':
        break
    try:
        fval = float(sval)
        if largest is None:
            largest = fval
        elif fval > largest:
            largest = fval
        if smallest is None:
            smallest = fval
        elif fval < smallest:
            smallest = fval
    except:
        print('bad data')
        continue
    num = num+1
    tot = tot+fval
print('all done')
print(tot,num,tot/num)
print("Largest value is",largest)
print("Smallest value is",smallest)
