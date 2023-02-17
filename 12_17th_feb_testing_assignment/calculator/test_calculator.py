from calculator import add , subtract , miltiply , divide
def test_add():
    assert add(2,3) == 5
    assert add(5,3) != 5
    assert add(2,0) == 2
    assert add(2.2,3) == 5.2
    

def test_subtract():
    assert subtract(3,2) == 1
    assert subtract(2,5) != 3
    assert subtract(5,0) == 5
    


def test_multiply():
    assert miltiply(3,2) == 6
    assert miltiply(2,5) != 4848
    assert miltiply(5,0) == 0
    
    

def test_divide():
    assert divide(6,2) == 3
    assert divide(5,3) != 5
    assert divide(2,0) == 1
    assert divide(10,2) == 5
    
