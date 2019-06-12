REVERSE 
def rev(s):
    s=s[::-1]
    return s

s=str(input())
print(rev(s))

FRREQUENCY OF A CHARACTER
from collections import OrderedDict
s=input()
l=sorted(s)
d=OrderedDict()
for i in l:
    d[i]=0
for i in l:
    d[i]+=1
for i in d:
    print(i,d[i])

LOWER TO UPPER
string=str(input())
print(string.swapcase())

Remove all Characters in a String except Alphabet:
def charalpha(s):
    newstr=""
    valid="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if i in valid:
            newstr+=i
    return newstr

s=str(input())
print(charalpha(s))

SPECIAL STRING AGAIN
