str= 'X-DSPAM-Confidence:0.8475'
cc=str.find(':')
print(cc)
bb=str.find(' ',cc)
print(bb)
aa=str[cc+1:]
print(aa)
zz=float(aa)
print(zz)
