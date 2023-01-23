
def add(a,b):
    return a+b 

def subtract(a,b):
    return a-b 
def Multiply(a,b):
    return a*b 
def Divide(a,b):
    try :
        print(a/b)
    except ZeroDivisionError :
        print("Exception is :-" , ZeroDivisionError )

print('Enter Numbers ')
a ,b = map(int , input().split() )
print('Enter The Operation') 
o = input() 

if o == "+":
    print(add(a,b)) 
elif o == '-':
    print(subtract(a,b)) 
elif  o == '*':
    print(Multiply(a,b)) 
else :
    print(Divide(a,b)) 
