def closest(n, a):
    b= a[0]
    for i in range (len (a)):
        if abs (n - a[i]) < abs (n - b):
            b = a[i]
    return b

arr =list(map(int,input().split()))
num =int(input()) 
print(closest(num, arr))
