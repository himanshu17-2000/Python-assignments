given = [1,2,3,1,3,4,6,5,3]
m = dict() 
n = {i : 1  for i in given } 
ans = [k for k ,v in n.items()] 
print(ans)
