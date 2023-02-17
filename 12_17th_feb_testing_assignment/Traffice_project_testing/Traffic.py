class Vehicle:
    def __init__(self, regno, color):
        self.color=color
        self.regno=regno


class Car(Vehicle):
    def __init__(self, regno, color):
        Vehicle.__init__(self, regno, color)

    def getType(self):
        return "Car"

class ParkingLot:
    def __init__(self):
        self.capacity = 0
        self.slot_id = 0
        self.occupied_slot = 0

    def create_parking_lot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity

    def get_empty_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i
            

    def park(self, regno, color):
        # print("New Car parking: " + str(regno) + str(color), self.occupied_slot, self.capacity)
        if self.occupied_slot < self.capacity:
            slot_id = self.get_empty_slot()
            self.slots[slot_id] = Car(regno, color)
            self.slot_id = self.slot_id + 1
            self.occupied_slot = self.occupied_slot + 1
            return slot_id + 1
        else:
            return -1

    def leave_slot(self, slot_id):
        # print(self.slots, self.slots[slot_id - 1], self.occupied_slot)
        if self.occupied_slot > 0 and self.slots[slot_id - 1] != -1:
            self.slots[slot_id - 1] = -1
            self.occupied_slot = self.occupied_slot - 1
            # print("Vacant slot: " + str(slot_id))
            return True
        else:
            # print("Empty slot: " + str(slot_id))
            return False

    def check_status(self):
        print("Slot No \tRegistration No \tColor")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i + 1) + "\t" + str(self.slots[i].regno) + "\t" + str(self.slots[i].color))
            else:
                continue

    def get_regno_from_color(self, color):
        regnos = []
        for i in self.slots:
            if i == -1:
                continue
            if i.color == color:
                regnos.append(i.regno)
        return regnos

    def get_slotno_from_regno(self, regno):
        for i in range(len(self.slots)):
            if self.slots[i]!= -1 and self.slots[i].regno == regno:
                print(i+1)
                return i+1
            else:
                continue
        return -1

    def get_slotno_from_color(self, color):
        slotnos = []
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i + 1))
        return slotnos

    def show_data(self, line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.create_parking_lot(n)
            print('Created a parking lot with ' + str(res) + ' slots')

        elif line.startswith('park'):
            regno = line.split(' ')[1]
            color = line.split(' ')[2]
            res = self.park(regno, color)
            if res == -1:
                print("parking lot is full")
            else:
                print('Allocated slot number: ' + str(res))
        elif line.startswith('leave_slot'):
            leave_slot_id = int(line.split(' ')[1])
            status = self.leave_slot(leave_slot_id)
            if status:
                print('slot number ' + ' ' + str(leave_slot_id) + 'is free')

        elif line.startswith('status'):
            self.check_status()

        elif line.startswith('regno_for_cars_with_colour'):
            color = line.split(' ')[1]
            regnos = self.get_regno_from_color(color)
            print(', '.join(regnos))

        elif line.startswith('slotno_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.get_slotno_from_color(color)
            print(', '.join(slotnos))

        elif line.startswith('slot_number_for_regno'):
            regno = line.split(' ')[1]
            slotno = self.get_slotno_from_regno(regno)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)


def main():
    parkinglot = ParkingLot()
    while True:
        line = input(">> ")
        parkinglot.show_data(line)


if __name__ == '__main__':
    main()