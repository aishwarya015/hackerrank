Given 2 arrays, count the number of pairs in the two arrays such that each pair has a distinct sum.
def pairs(a,b):
    c=0
    list1=[]
    for i in arr:
        for j in arr2:
            if(i+j not in list1):
                c=c+1
                list1.append(i+j)
    return c
a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(pairs(arr,arr2))

input
2 1
3 2
3
Output 
2


##Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#i/p:1 3 5 4 7
#o/p:3

def lenOfLongIncSubArr(arr, n) :  
    m = 1
    l = 1
    for i in range(1, n) : 
        if (arr[i] > arr[i-1]) : 
            l =l + 1
        else :  
            if (m < l) : 
                m = l 
            l = 1
    if (m < l) : 
        m = l 
    return m 
arr =[int(i) for i in input().split()]
#print(arr)
n = len(arr) 
print(lenOfLongIncSubArr(arr, n)) 

#Given an array A of N positive integers. The task is to swap every ith element of the array with (i+2)th element.
length=int(input())
list1=list(map(int,input().rstrip().split()))
for i in range(0,len(list1)-2):
    list1[i],list1[i+2]=list1[i+2],list1[i]
for i in list1:
    print(i,end=' ')
   ##i/p:5
         1 2 3 4 5
   ##o/p:3 4 5 2 1

##Print the maximum sum of the non-contiguous subarrays of the given array.
num1=int(input())
list1=list(map(int,input().rstrip().split()))
sum=0
for i in list1:
    if sum+i>sum:
        sum+=i
print(sum)
##i/p:5
      9 -8 5 -2 7
##o/p:21(9+5+7)


GCD
n=int(input())
ar=list(map(int,input().split()))
ar2=[]
ar3=[]
def gcd(a,b):
    if(a>b):
        a=a%b
    else:
        a=b%a
    return a
for i in range(n): 
    for j in range(n):
        if(i!=j):
            ar2.append(ar[j])
    a=ar2[0]
    b=ar2[1]
    g=gcd(a,b)
    for k in range(2,len(ar2)):
        g=gcd(g,ar2[k])
    ar3.append(g)
    ar2.clear()
print(max(ar3))

Write a program to print sum of numbers which are not in the edges of the matrix.
a=int(input())
b=int(input())
s=0
m=[[0]*b]*a
m=[[int(input())for i in range (b)]for j in range (a)]
if(b<=2 and a<=2):
    s=-1
else:
    for i in range(1,a-1):
        for j in range(1,b-1):
            s+=m[i][j]
print(s)
            

