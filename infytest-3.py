infy-10
def string_both_ends(input_string):
    if(len(input_string)<2):
        return -1
    else:
        s=""
        s=input_string[0:2]+input_string[len(input_string)-2:len(input_string)]
        return s

input_string=input("")
print(string_both_ends(input_string))

infy-11
def find_upper_and_lower(sentence):
    upper=0
    lower=0
    for i in sentence:
        if(i>="a" and i<="z"):
            lower+=1
        if(i>="A" and i<="Z"):
            upper+=1
        result_list=[]
        result_list.append(upper)
        result_list.append(lower)
    return result_list

sentence=input("")
print(find_upper_and_lower(sentence))

infy-12
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in subjects:
        for j in verbs:
            for k in objects:
                sentence_list.append(i+" "+j+" "+k)
    return sentence_list
subjects=list(input().split())
verbs=list(input().split())
objects=list(input().split())
print(*generate_sentences(subjects,verbs,objects),sep="\n",end="")

infy-13
import math
def close_number(num1,num2,num3):
    if math.fabs(num1-num2)==1 and math.fabs(num3-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num3-num2)==1 and math.fabs(num1-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num1-num3)==1 and math.fabs(num3-num2)>=2 and math.fabs(num2-num1)>=2:
        return True
    else:
        return False
num1,num2,num3=map(int,input().split())
print(close_number(num1,num2,num3))

infy-14
def find_five_digit():
    num2=0
    num3=0
    num4=0
    num5=0
    for i in range(9,-1,-1):
        num2=int(i-2)
        num3=int(num2-2)
        num4=int(num3-2)
        num5=int(num3)
        if(num3+num4+num5==i and num2+num3+num4+num5+i==19):
            break
    s=str(i)+str(num2)+str(num3)+str(num4)+str(num5)
    print(s)

find_five_digit()
