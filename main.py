#!/usr/bin/env python2

import array
import math
import itertools
num="152487216054048971758341586351234728397473961424346"
mod = 4 #divide 0-9 in groups of mod
maxinum = 9 
f1=open('plaintext','w')
f1.write(num)
f1.close()
f2=open('binary','wb')
#mod = 2^n. Finding value of n
#n defines the size of each block
n = int(math.log(mod,2))
positions=''
output=[''] * (maxinum/mod + 1+1+1 )
for x in num:
    line = (int(x)/mod)+1
    print x,line
    output[1] += '1'*line+'0'
    binterm=bin(int(x)).split('b')[1]
    output[line+1] += '0'*(n-len(binterm))+binterm[-n:]

for i in range(0,len(output)):
    line=output[i]
    if line!='':
        output[i] = output[i] +  ( '0'*(8-len(line)%8) if (len(line)%8) else '')
        #print output[i], len(line), len(line)%8
        output[0] += str(len(output[i])/8)+' '

output[0]=output[0].strip()
f2.write(output[0]+'\n')
def grouper(n,iterable):
    args=[iter(iterable)]*n
    return itertools.izip_longest(fillvalue=None,*args)
for i in range(1,len(output)):
    g=(grouper(8,output[i]))
    for x in g:
        print x, int(''.join(x),2)
        f2.write(chr(int(''.join(x),2)))
f2.close()
