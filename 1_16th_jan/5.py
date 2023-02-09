
import os 
import sys 
file = open(os.path.join(sys.path[0], "hash.txt"), mode ='w')
file.write('THE WORLD IS NOT FLAT')
file = open(os.path.join(sys.path[0], "hash.txt"), mode ='r')
s1 = ''
for line in file :
    for i in line:
        s1 += i 
        s1 += '#' 
    
print(s1)
file.close()