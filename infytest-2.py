infy-04
def find(num):
    for i in range(0,len(num)):
        if(num[i]==9 and i<4):
            return True
    return False
num=list(map(int,input().split()))
print(find(num))

infy-05
def countdigits(s):
    l=[]
    c1=0
    c2=0
    for i in s:
        if(i.isalpha()):
            c1+=1
        if(i.isdigit()):            
            c2+=1
    l.append(c1)
    l.append(c2)
    return l
s=input()
print(countdigits(s))

infy-31
def sum(num_list,number):
    a=len(num_list)
    result_sum=0
    for i in range(1,a-1):
        if(num_list[i-1]!=number and num_list[i+1]!=number and num_list[i]!=number):
            result_sum+=num_list[i]
    if(num_list[1]!=number and num_list[0]!=number):
        result_sum+=num_list[0]
    if(num_list[a-2]!=number and num_list[a-1]!=number):
        result_sum+=num_list[a-1]
    return result_sum
      
num_list=list(map(int,input().split()))
number=int(input())
print(sum(num_list,number))

infy-06
def check(l):
    num = ""
    for i in l:
        num = num + str(i)
    if "123" in num:
        return True
    else:
        return False
l=list(map(int,input().split()))
print(check(l))

infy-29
def exchange_list(number_list):
    d=len(number_list)
    a=len(number_list)//2
    b=a//2+a
    k=0
    for i in range(a,b):
        c=number_list[i]
        number_list[i]=number_list[d-k-1]
        number_list[d-k-1]=c
        k=k+1
    for i in range(a):
        temp=number_list[i]
        number_list[i]=number_list[i+a]
        number_list[i+a]=temp
    return number_list
l=list(map(int,input().split()))
print(*exchange_list(l))
