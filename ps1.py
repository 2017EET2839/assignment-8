###### this is the first .py file ###########

import copy
####### write your code here ##########
inp = raw_input("Enter two values:  ").split()
n = int(inp[0])
m = int(inp[1])
a=[]
str1=[]
for i in range(n):
    l = raw_input("Enter the list")
    for j in range(len(l)):
        str1.append(l[j])
        str2=copy.copy(str1)
    a+=[str2]
    del str1[0:len(str1)]
print(a)
Matrix1 = [[0 for x in range(n)] for y in range(m)] 
for x in range(n):
    for y in range(m):        
        if(a[x][y]=='S'):
           Matrix1[x][y] = 1
        else:
           Matrix1[x][y] = 0
max=0
valid=1
for x in range(n):
    for y in range(m):        
        if(Matrix1[x][y]==1):
            start=0
            valid=1
            while (valid==1):
                if(x>=start and Matrix[x-start][y]==1):
                    pass
                else:
                    valid=0         
                if(y>=start and Matrix[x][y-start]==1):
                    pass
                else:
                    valid=0
                if(x+start<n and Matrix[x+start][y]==1):
                    pass
                else:
                   valid=0         
                if(y+start<m and Matrix[x][y+start]==1):
                    pass
                else:
                    valid=0
                start=start+1
            print(start,x,y)
