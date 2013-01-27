#!/usr/bin/env python2

import array
import math
import itertools
#num="152487216054048971758341586351234728397473961424346"
num="152472160540471753415635123472374736142434611564879462125641652562165487921564987923131636662156898716654987213223165479879542136464989878921321611321111111165496498469612132165654231363231645648931632156"
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
output[0]=str(mod)+' ';
for i in range(1,len(output)):
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

#Decoding
f3 = open('binary','rb')
#first line tells us the number of characters on each level
fline=f3.readline()
#each value is separated by a space, split by spaces
numChars=fline.split(' ')
#form input array:
finput=[]
for x in numChars[1:]:
    finput.append(f3.read(int(x)))
#the first value in fline will give us the input mod
f3.close()
mod = int(numChars[0])
n = int(math.log(mod,2))
#we have the input from the file, we now need to decode it
#first line describes the position of each number. Each position is written in the form of ones. Each position is separated by a '0' So, 101110111101011 will give [1,3,4,1,2]
#output = ''
#build binary from ascii
binaryLines=['']*len(finput)
for line in range(0,len(finput)):
    binline=''
    for x in finput[line]:
        binterm=bin(ord(x)).split('b')[1]
        binline+= '0'*(8-len(binterm)) + binterm
    binaryLines[line]=binline
    
positions = filter(bool,binaryLines[0].split('0'))
outputnum=''
for pos in positions:
    line = pos.count('1')
    outputnum+=str(int(bin(line-1).split('b')[1] + binaryLines[line][0:n],2))
    binaryLines[line]=binaryLines[line][n:]
f4 = open('decodedPlainText','w')
f4.write(outputnum)
f4.close()
