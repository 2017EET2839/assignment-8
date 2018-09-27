###### this is the first .py file ###########
#!/usr/bin/python
import sys
import copy
####### write your code here ##########
inp = input("Enter two values:  ").split(" ")
#inp = raw_input("Enter two values:  ").split()
#give input to the 
n = int(inp[0])
m = int(inp[1])
#a list
a=[]
str1=[]
#get the list 
for i in range(n):
    #l = input("Enter the list")
    l = input("Enter the list")
    for j in range(len(l)):
        str1.append(l[j])
        str2=copy.copy(str1)
    a+=[str2]
    del str1[0:len(str1)]
#print(a)
#new matrix
Matrix1 = [[0 for x in range(m)] for y in range(n)] 
for x in range(n):
    for y in range(m):        
        if(a[x][y]=='S'):
           Matrix1[x][y] = 1
        else:
           Matrix1[x][y] = 0
#max2 and max1 are maximums top 2
max2=0
max1=0
mat=[]
valid=1
# to find out the cross in the matrix
for x in range(n):
    for y in range(m):        
        if(Matrix1[x][y]==1):
            start=0
            valid=1
            while (valid==1):
                if(x>=start):
                    if(Matrix1[x-start][y]==1):
                        pass
                    else:
                        valid=0    
                        break
                else:
                    valid=0         
                    break
                
                if(y>=start):
                    if(Matrix1[x][y-start]==1):
                        pass
                    else:
                        valid=0
                        break
                else:
                    valid=0
                    break

                if(x+start<n):
                    if(Matrix1[x+start][y]==1):
                        pass
                    else:
                        valid=0             
                        break
                else:
                    valid=0  
                    break
                if(y+start<m):
                    if(Matrix1[x][y+start]==1):
                        pass
                    else:
                        valid=0
                        break
                else:
                    valid=0
                    break
                start=start+1
            if(max2<max1 and max1<start):
                max2=max1
            if(max1<start):
                max1=start
            mat+=[start]
            #print(start,x,y)
print(4*(max1-1)+1,4*(max2-1)+1)
#print(mat)

    