import csv
import os
import sys 
# file =  open(os.path.join(sys.path[0], "data.csv"), "r")
# for i in file :
#   print(i)

# person = [] 
# opening the CSV file
with open(os.path.join(sys.path[0], "data.csv"), mode ='r')as file:
# with open('data.csv', mode ='r') as file :

  # reading the CSV file
 
  # displaying the contents of the CSV file
  print(file.read())

    


  
