##infy21
def check_numbers(num1,num2):
    num_list=set()
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.add(i)
    count=len(num_list)
    return [num_list,count]
num1,num2=map(int,input().split())
print(check_numbers(num1, num2))

##Reverse a digit
#include <iostream>  
using namespace std;  
int main()  
{  
long n, reverse=0, rem;        
cin>>n;    
  while(n!=0)    
  {    
     rem=n%10;      
     reverse=reverse*10+rem;    
     n/=10;    
  }    
 cout<<reverse<<endl;     
return 0;  
}  

##calculate the product of digits

def getProduct(n): 
  
    product = 1
  
    while (n != 0): 
        product = product * (n % 10) 
        n = n // 10
  
    return product 
  
n =int(input())
print(getProduct(n)) 

##Prime or Not
#**in c **#
#include <stdio.h>
int main()
{
    int n, i, flag = 0;


    scanf("%d", &n);

    for(i = 2; i <= n/2; ++i)
    {
    
        if(n%i == 0)
        {
            flag = 1;
            break;
        }
    }
        if (flag == 0)
          printf("Yes");
        else
          printf("No");
    
    
    return 0;
}
##Armstrong no
num = int(input())

sum = 0
order=len(str(num))

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print("Yes")
else:
    print("No")
    
###Print Fibonacci numbers till n

num = int(input())
first= 0
second= 1
 
print(first, second,end=" ")
 
for i in range(2, num):
    next = first + second
    print(next, end=" ")
 
    first = second
    second = next
