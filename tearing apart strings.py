stringul = 'X-DSPAM-Confidence: 0.8475'
x = stringul.find(":")
print(x)
y = stringul[x+1:]
print(y)
z = float(y)
print(z)