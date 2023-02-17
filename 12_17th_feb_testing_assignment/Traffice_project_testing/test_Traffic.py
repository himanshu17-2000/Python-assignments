import pytest 
from Traffic import ParkingLot , Vehicle ,Car
parkobj = ParkingLot() 
parkobj.create_parking_lot(10)
print(parkobj.slots)
empty_slot = parkobj.get_empty_slot()
s1_id = parkobj.park(10 , 'green')
s3_id = parkobj.park(30 , 'blue')
s2_id = parkobj.park(20 , 'red')
parkobj.leave_slot(s2_id)
print(parkobj.slots)
def test_create_parking_Lot_valid(): 
    assert parkobj.capacity == 10
    assert parkobj.capacity != 20

def test_get_empty_slot():
   slot = parkobj.get_empty_slot() 
   assert (parkobj.slots[slot] == -1)
   assert (parkobj.slots[0] != -1) 
   assert (parkobj.slots[3] == -1)

def test_get_empty_slot():
   assert parkobj.park(40 , 'black') != -1
   assert  0 <= parkobj.park(40 , 'black') <= parkobj.capacity 

def test_get_regno_from_color():
   assert parkobj.get_regno_from_color('green') != []
   assert parkobj.get_regno_from_color('red') == []


def test_get_slotno_from_regno():
   assert parkobj.get_slotno_from_regno(10) == 1
   assert parkobj.get_slotno_from_regno(20) == -1

def test_get_slotno_from_color():
    assert parkobj.get_slotno_from_color('green') != []
    assert parkobj.get_slotno_from_color('red') == []

def test_leave_Slot():
   assert parkobj.leave_slot(1)  == True
   assert parkobj.leave_slot(1)  == False






