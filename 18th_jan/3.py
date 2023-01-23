def counter_yeild():
    i = 0 
    while(True):
        yield i
        i += 1 

x = counter_yeild()

print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Use Case :-  we can attach a event say click and on click we can call this function next(x),
# thus would yeild a value which we can use to display on screen 
# and we can use this generator in such way 

