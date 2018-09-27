###### this is the second .py file ###########

#rotate function
#input : list an l and length n
#output : rotate the list by  n and return the output list
def rotate(l, n):
    return l[n:] + l[:n]


#!/usr/bin/python
####### write your code here ##########
#get input
inp = input("Enter three values:  ").split(" ")
#divide it into 3 parts
k1 = int(inp[0])
k2 = int(inp[1])
k3 = int(inp[2])

# different parts regular expressions for matching
part1=[]
part1+='abcdefghi'        #one of the alphabets
part2=[]
part2+='jlkmnopqr'        #one of the alphabets
part3=[]
part3+='stuvwxyz_'       #one of the alphabets
#for 3 parts of the string accordint to 3 regular exp
str1=[]
str2=[]
str3=[]
#input string
string = input("Enter the string:  ")
#convert to string
string=list(string)
#divide the string into 3 parts
for i in range(len(string)):
    if string[i] in part1:
        str1+=string[i]
        pass
    if string[i] in part2:
        str2+=string[i]
        pass
    if string[i] in part3:
        str3+=string[i]
        pass
#print(str1)
rotate(str1, k1)
#print(str2)
rotate(str2, k2)
#print(str3)
rotate(str3, k3)
#rotating the entire string according to developed lists
l=0
m=0
n=0
for i in range(len(string)):
    if string[i] in part1:
        #print(part1.index(string[i]))
        string[i]=str1[(l-k1)%len(str1)]
        l+=1
        pass
    if string[i] in part2:
        string[i]=str2[(m-k2)%len(str2)]
        m+=1
        pass
    if string[i] in part3:
        string[i]=str3[(n-k3)%len(str3)]
        n+=1
        pass
final_output = ''.join(string)
#print the final output
print(final_output)

    