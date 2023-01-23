def divison(*args):
    for i in args:
        a = i[0]
        b = i[1]
        try :
            print(a/b)
        except  ZeroDivisionError:
            print(ZeroDivisionError) 
        except TypeError  :
            print(TypeError) 


# Given [[1, 0], [1, 2], [6, 3], [1, “a”] ]
divison([1, 0], [1, 2], [6, 3], [1, "a"] )




