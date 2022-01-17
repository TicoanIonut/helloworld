import random
lower = 'abcdefghijklmnopqrstyuvxz'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
number = '1234567890'
symbol ="?!;:'*/)(+-&_$#@"
all = lower+upper+number+symbol
lenght =13
password ="".join(random.sample(all,lenght))
print('Password:',password )
