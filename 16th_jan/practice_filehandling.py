import sys
import os 

file = open(os.path.join(sys.path[0], "test2.txt"), mode ='w')
print('Tell me No. of lines you want to add ') 
n = int(input()) 
for i in range(n):
    print("Enter the String:-")
    n = str(input()) 
    file.write(n+"\n")
 
file = open(os.path.join(sys.path[0], "test2.txt"), mode ='r')
for i in file :
    print(i)  
file.close() 
