LEFT ROTATION
b,a=list(map(int,input().split()))
l=list(map(int,input().split()))
li=[]
for i in range(a,len(l)):
    li.append(l[i])
for i in range(0,a):
    li.append(l[i])
    
print(*li)
##i/p:
5 4
1 2 3 4 5
#o/p:5 1 2 3 4

NUMTOROMAN
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

n=int(input())
print(py_solution().int_to_Roman(n))
#i/p:3
#o/p:III

infy-friday
def reverse(num):

    return int(str(num)[::-1])

def palindrome(num):

    for i in range(100):
        rnum = reverse(num)
        if rnum == num:
            break
        num = num + rnum
    return i,num
num=int(input())
print(*palindrome(num), sep=" ")


##i/p:195
##o/p:4 9339
##The reverse and add function starts with a number, reverses its digits, and adds the reverse to the original. If the sum is not a palindrome (meaning it does not give the same number read from left to right and right to left), we repeat this procedure until it does.

For example, if we start with 195 as the initial number, we get 9,339 as the resulting palindrome after the fourth addition:

 195  786    1,473  5,214
 591  687    3,741  4,125
+___ +_____ +_____ +_____
786   1,473  5,214  9,339
This method leads to palindromes in a few steps for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It has never been proven, however, that no such palindrome exists. You must write a program that takes a given number and gives the resulting palindrome (if one exists) and the number of iterations/additions it took to find it. 
