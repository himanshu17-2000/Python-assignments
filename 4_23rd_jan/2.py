given = [1, "a" , 2 , "b" , 3 , "c"]

print(list(filter(lambda i : i in [1,2,3,4,5,6,7,8,9,0] ,given)))

print(list(filter(lambda i : i not in [1,2,3,4,5,6,7,8,9,0] ,given)))