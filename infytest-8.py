AMSTRONG INTERVAL
a=int(input())
b=int(input())
for i in range (a,b+1):
    o=len(str(i))
    rem=0
    temp=i
    while temp>0:
        number=temp%10
        rem+=number**o
        temp=temp//10
    if rem==i:
        print(i)
  
LONGEST INCREASING SUBSEQUENCE 
