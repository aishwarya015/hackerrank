infy-01
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
str=input("")
print(add_string(str))

infy-46
n=list(map(int,input().split()))
print(0,end=" ")
for i in range(1,len(n)):
    print(n[i-1]*2,end=" ")
    
infy-38
r,c=map(int,input().split())
l=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        temp=str(i)+","+str(j)
        n.append(temp)
    l.append(n)
print("[",end="")
print(*l,sep=",\n",end="")
print("]")

infy-03
import ast
def create_new_dictionary(prices):
    n=ast.literal_eval(prices)
    new_dict={}
    for key,value in n.items():
        if value>200.0:
            new_dict[key]=value
    sorted_d=sorted(new_dict.items()) 
    return dict(sorted_d)
prices=input()
print(create_new_dictionary(prices))

BALANCED BRACKETS
def isValidPair(left,right):
    if left=='(' and right==')':
        return True
    if left=='{' and right=='}':
        return True
    if left=='[' and right==']':
        return True
    return False
def isProperlyNested(S):
    stack=[]
    
    for symbol in S:
        if symbol=='[' or symbol=='{' or symbol=='(':
            stack.append(symbol)
        else:
            if len(stack)==0:
                return False
            last =stack.pop()
            if not isValidPair(last,symbol):
                return False
    if len(stack)!=0:
        return False
    return True
N=int(input())
for _ in range(N):
    s=input()
    if isProperlyNested(s):
        print("YES")
    else:
        print("NO")
