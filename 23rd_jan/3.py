given = [1,2,3,1,3,4,6,5,3]
m = dict() 
for i  in given:
    if(i not in m):
        m[i] = 1 
n = {i : 1  for i in given if(not i)} 
ans = [k for k ,v in n.items()] 
print(ans)
