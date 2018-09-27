###### this is the second .py file ###########
def rotate(l, n):
    return l[n:] + l[:n]


#!/usr/bin/python
1 1 1####### write your code here ##########
inp = raw_input("Enter three values:  ").split()
k1 = int(inp[0])
k2 = int(inp[1])
k3 = int(inp[2])

#
part1=[]
part1+='abcdefghi'
part2=[]
part2+='jlkmnopqr'
part3=[]
part3+='stuvwxyz_'
str1=[]
str2=[]
str3=[]
string = raw_input("Enter the string:  ")
string=list(string)
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
m=0
l=0
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
print(final_output)

    