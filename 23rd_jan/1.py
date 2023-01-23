arr = ["name512" , "same1example" , "joy18full"] 
for j  in range(len(arr)) :
    t = ""
    for i in arr[j] :
        if( i >= 'a' and i <= 'z'):
            t+= i 
    arr[j] = t 

print(arr)
    


